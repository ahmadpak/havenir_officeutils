// Copyright (c) 2019, Havenir and contributors
// For license information, please see license.txt

frappe.ui.form.on("Supplier Balance Comparison", {
  supplier: function(frm) {
    var doc = cur_frm.doc;
    if (doc.compared_up_to) {
      frm.trigger("compared_up_to");
    }
  },

  compared_up_to: function(frm, cdt, cdn) {
    var doc = cur_frm.doc;
    console.log(doc.compared_up_to);
    if (!doc.supplier) {
      frappe.throw("Please select Supplier!");
    } else {
      frm.call({
        method: "erpnext.accounts.utils.get_balance_on",
        args: {
          date: doc.compared_up_to,
          party_type: "Supplier",
          party: doc.supplier,
          company: doc.company
        },
        callback: function(r) {
          frappe.model.set_value(cdt, cdn, "our_balance", r.message);
          //cur_frm.refresh_field('call_details');
        }
      });
    }
  }
});
