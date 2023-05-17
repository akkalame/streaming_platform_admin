// Copyright (c) 2023, Akkalame Ereut and contributors
// For license information, please see license.txt

 frappe.ui.form.on("Platform Profile", {
	refresh(frm) {
		// coloco una fecha de vencimiento al iniciar un nuevo formulario
		if (!frm.doc.due_date || frm.doc.due_date == ''){
			var today = frappe.datetime.get_today();
			var next_month = frappe.datetime.add_months(today, 1);
			frm.doc.due_date = next_month;
			frm.refresh_field('due_date');
		}
	},

 	platform(frm){
 		frm.set_query("platform_account", function() {
        return {
            "filters": [
                ["Platform Account", "platform", "=", frm.doc.platform],
                ["Platform Account", "available_profiles", "!=", 0]
            ]
        };
    });
 	}
});
