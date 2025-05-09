# Copyright (c) 2025, TDT and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestDriver(FrappeTestCase):
    def test_full_name_correctly_set(self):
        test_driver = frappe.get_doc({
            "doctype": "Driver",
            "first_name": "John",
            "last_name": "Doe",
            "lincense_number": "LIC12345"
            })
        test_driver.save()  # Dòng 14
        self.assertEqual(test_driver.full_name, "John Doe")
