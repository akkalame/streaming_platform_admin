# Copyright (c) 2023, Akkalame Ereut and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Platform(Document):
	pass

def get_price_profiles_rules(platform=None):
	sql = """
		SELECT 
	"""


