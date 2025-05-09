# Copyright (c) 2025, TDT and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Driver(Document):
	def before_save(seft):
		seft.full_name = seft.first_name + " " + seft.last_name

# API key 080546ced607302
# # Save API Secret: 49c0c67a7430fad