# Copyright (c) 2023, Akkalame Ereut and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils.response import build_response

class PlatformAccount(Document):
	def before_insert(self):
		# verifica que no exista el mismo usuario con la misma plataforma 
		nSameRecord = frappe.db.count('Platform Account', 
			{
				'platform':self.platform,
				'username': self.username
			})
		if nSameRecord > 0:
			frappe.throw('This username already exist in that platform')




@frappe.whitelist()
def get_max_profile_qty(platform):
	profile_qty = frappe.db.get_value('Platform', platform, 'profile_qty')
	frappe.local.response.update({
		"profile_qty": profile_qty
	})
	return build_response("json")