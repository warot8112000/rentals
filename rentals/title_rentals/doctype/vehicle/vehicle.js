// Copyright (c) 2025, TDT and contributors
// For license information, please see license.txt

frappe.ui.form.on("Vehicle", {
	refresh(frm) {

	},
    get_summary(frm){
        cur_frm.get_field("summary").$wrapper.append("<h1>He is your summary</>");
    }
});
