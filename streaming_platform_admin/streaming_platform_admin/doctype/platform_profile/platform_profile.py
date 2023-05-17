# Copyright (c) 2023, Akkalame Ereut and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class PlatformProfile(Document):
	def before_insert(self):
		account_doc = frappe.get_doc('Platform Account', self.platform_account)
		if account_doc.available_profiles == 0:
			frappe.throw("This platform account hasn't available profile")

	def after_insert(self):
		account_doc = frappe.get_doc('Platform Account', self.platform_account)
		if account_doc.available_profiles > 0:
			account_doc.available_profiles -= 1
			account_doc.save()