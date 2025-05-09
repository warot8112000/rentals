# Copyright (c) 2025, TDT and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document


class RideBooking(Document):
	def validate(seft):
		if not seft.rate:
			seft.rate = frappe.db.get_single_value("Rentals Settings", "standard_rate")
			
		total_distance = 0
		for item in seft.items:
			total_distance += item.distance

		seft.total_amount = total_distance * seft.rate

