# Copyright (c) 2025, TDT and contributors
# For license information, please see license.txt

# import frappe


import frappe


def execute(filters=None):
    columns = [
        {
            "fieldsname": "make",
            "label": "Make",
            "fieldtype": "Data",
        },
        {
            "fieldsname": "total_revenue",
            "label": "Total Revenue",
            "fieldtype": "Currency",
            "options": "AED",
        },
    ]
    data = frappe.get_all(
        "Ride Booking",
        fields=["SUM(total_amount) AS total_revenue", "vehicle", "vehicle.make"],
        filters={"docstatus": 1},
        group_by="make",
    )

    chart = {
        "data": {
            "labels": [x.make for x in data if x.make],  
            "datasets": [
                {
                    "name": "Total Revenue",
                    "values": [
                        float(x.total_revenue or 0) for x in data if x.make
                    ], 
                }
            ],
        },
        "type": "pie",
    }

    return columns, data, "Here is report", chart
