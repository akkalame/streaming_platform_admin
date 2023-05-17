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
		SELECT pa.supplier, s.mobile_no, p.platform_name, pa.username, pa.due_date, pa.price
		FROM `tabPlatform Account` pa
			JOIN tabPlatform p ON pa.platform = p.name
			JOIN `tabSupplier` s ON pa.supplier = s.name
		WHERE pa.owner = '{0}'
		ORDER BY pa.due_date ASC
		""".format(frappe.session.user)

	query = frappe.db.sql(sql, as_dict=True)
	return query

def format_data(raw_data, filters):

	data = []
	for rd in raw_data:
		aux = {
			"platform_name": rd.platform_name,
			"username": rd.username,
			"supplier": rd.supplier,
			"supplier_phone": rd.supplier_phone or '',
			"due_date": rd.due_date,
			"due_days": (getdate() - rd.due_date).days,
			"amount":rd.price

		}

		data.append(aux)

	return data

def get_columns(filters):
	columns = [
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
			'fieldname': 'supplier',
			'label': _('Supplier'),
			'fieldtype': 'Link',
			'options': 'Supplier',
			'width': 150
		},
		{
			'fieldname': 'supplier_phone',
			'label': _('Phone'),
			'fieldtype': 'Data',
			'width': 150
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