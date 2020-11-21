// Copyright (c) 2019, Havenir and contributors
// For license information, please see license.txt

frappe.ui.form.on('Payment Recovery Calls Customer', {
	customer: function(frm,cdt,cdn) {
		var doc = cur_frm.doc;
		var customertmp = frappe.model.get_doc(cdt,cdn);
		if (customertmp.customer){
			frm.call({
				method: 'erpnext.accounts.utils.get_balance_on',
				args: {
					date: frappe.datetime.get_today(),
					party_type: 'Customer',
					party: customertmp.customer,
					company: doc.company
				},
				callback: function(r){
					frappe.model.set_value(cdt,cdn,'balance',r.message);
					//cur_frm.refresh_field('call_details');
				}
			})
			frm.call({
				method: 'havenir_officeutils.office_utils.doctype.payment_recovery_calls.payment_recovery_calls.get_last_paid_amount',
				args: {
					customer: customertmp.customer
				},
				callback: function(r){
					frappe.model.set_value(cdt,cdn,'last_paid_amount',r.message.last_payment_amount);
					frappe.model.set_value(cdt,cdn,'last_payment_date',r.message.last_payment_date);
					frappe.model.set_value(cdt,cdn,'current_rating',r.message.rating);
				}
			})

			frappe.call('havenir_officeutils.office_utils.doctype.payment_recovery_calls.payment_recovery_calls.get_contract', 
			{party: customertmp.customer})
            .then (r => {
                if (r.message) {
                    frappe.model.set_value(cdt, cdn, 'contact', r.message)
					frm.refresh_fields('call_details')
                }
            })
		}
	},

	contact: function(frm, cdt, cdn) {
		var customertmp = frappe.model.get_doc(cdt,cdn);
		if (customertmp.contact) {
			frappe.call('havenir_officeutils.office_utils.doctype.payment_recovery_calls.payment_recovery_calls.set_phone',
				{contact: customertmp.contact})
				.then (r => {
					if (r.message) {
						frappe.model.set_value(cdt, cdn, 'contact_no', r.message)
						frm.refresh_fields('call_details')
					}
				})
		}
	}
});
