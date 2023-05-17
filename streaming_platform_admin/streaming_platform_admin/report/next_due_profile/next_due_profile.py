# Copyright (c) 2023, Akkalame Ereut and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import getdate

def execute(filters=None):
	columns, data = get_columns(filters), format_data(get_data(filters), filters)
	return columns, data

def get_data(filters):
	sql = """
		SELECT pf.customer, c.mobile_no, p.platform_name, pa.username, pf.profile, pf.due_date
		FROM `tabPlatform Profile` pf
			JOIN tabPlatform p ON pf.platform = p.name
			JOIN `tabPlatform Account` pa ON pf.platform_account = pa.name
			JOIN `tabCustomer` c ON pf.customer = c.name
		WHERE pf.owner = '{0}'
		ORDER BY pf.due_date ASC
		""".format(frappe.session.user)

	query = frappe.db.sql(sql, as_dict=True)
	return query

def format_data(raw_data, filters):
	platforms = frappe.get_list('Platform')
	platform_price_rules = {}
	for platform in platforms:
		platform_doc = frappe.get_doc('Platform', platform.name)
		platform_price_rules[platform_doc.platform_name] = {}
		for rule in platform_doc.price_profile:
			platform_price_rules[platform_doc.platform_name][rule.profile_qty] = rule.price


	data = []
	for rd in raw_data:
		aux = {
			"customer": rd.customer,
			"customer_phone": rd.customer_phone or '',
			"platform_name": rd.platform_name,
			"username": rd.username,
			"profile": rd.profile,
			"due_date": rd.due_date,
			"due_days": (getdate() - rd.due_date).days,
			"amount": platform_price_rules[rd.platform_name][1] or 0

		}

		data.append(aux)

	return data

def get_columns(filters):
	columns = [
		{
			'fieldname': 'customer',
			'label': _('Customer'),
			'fieldtype': 'Link',
			'options': 'Customer',
			'width': 150
		},
		{
			'fieldname': 'customer_phone',
			'label': _('Phone'),
			'fieldtype': 'Data',
			'width': 150
		},
		{
			'fieldname': 'platform_name',
			'label': _('Platform'),
			'fieldtype': 'Data',
			'width': 100
		},
		{
			'fieldname': 'username',
			'label': _('Username'),
			'fieldtype': 'Data',
			'width': 250
		},
		{
			'fieldname': 'profile',
			'label': _('Profile'),
			'fieldtype': 'Data',
			'width': 120
		},
		{
			'fieldname': 'due_date',
			'label': _('Due Date'),
			'fieldtype': 'Date',
			'width': 100
		},
		{
			'fieldname': 'due_days',
			'label': _('Due Days'),
			'fieldtype': 'Int',
			'width': 100
		},
		{
			'fieldname': 'amount',
			'label': _('Amount'),
			'fieldtype': 'Currency',
			'width': 120
		},
	]
	return columns