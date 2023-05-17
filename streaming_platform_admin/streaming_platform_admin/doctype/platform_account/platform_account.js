// Copyright (c) 2023, Akkalame Ereut and contributors
// For license information, please see license.txt

frappe.ui.form.on("Platform Account", {
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
		// obtengo la cantidad maxima de perfiles para una plataforma
		frappe.call(
			'streaming_platform_admin.streaming_platform_admin.doctype.platform_account.\
			platform_account.get_max_profile_qty', {
	    platform: frm.doc.platform
			}).then(r => {
			    frm.doc.available_profiles = r.profile_qty;
			    frm.refresh_field('available_profiles');
		});
	}
});

function add_month(fecha){
	// Sumarle un mes a la fecha actual
	fecha.setMonth(fecha.getMonth() + 1);
	// Obtener los componentes de la nueva fecha
	var nuevoMes = fecha.getMonth() + 1; // Sumamos 1 ya que los meses en JavaScript se indexan desde 0
	var nuevoDia = fecha.getDate();
	var nuevoAnio = fecha.getFullYear();

	// Formatear la nueva fecha como string en formato "dd-mm-yyyy"
	var nuevaFecha = nuevoDia.toString().padStart(2, '0') + '-' + nuevoMes.toString().padStart(2, '0') + '-' + nuevoAnio;
	return nuevaFecha;
}