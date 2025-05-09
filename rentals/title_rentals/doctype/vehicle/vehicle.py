# Copyright (c) 2025, TDT and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class Vehicle(WebsiteGenerator):
	def before_save(seft):
		seft.title = f"{seft.make} {seft.model} {seft.year}"
