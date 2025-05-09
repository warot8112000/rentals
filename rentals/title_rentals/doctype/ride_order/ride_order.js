// Copyright (c) 2025, TDT and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
    onload(frm){
        console.log("Runing");
    },
    setup(frm) {
        console.log("Setting up");        
    },
	refresh(frm) {
        console.log("Refreshing");
        if (frm.doc.status == "New" ){
            frm.add_custom_button(("Accept"), () =>{
            // set status: accept
            frm.set_value("status", "Accepted");
            frm.save();
            }, "Actions")
            frm.add_custom_button(("Rejected"), () =>{
                // set status: accept
                frm.set_value("status", "Rejected");
                frm.save();
            }, "Actions")
        }                
	},
    status(frm) {
        console.log("Status changed");
    }
});
