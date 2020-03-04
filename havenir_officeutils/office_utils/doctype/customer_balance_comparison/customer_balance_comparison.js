// Copyright (c) 2019, Havenir and contributors
// For license information, please see license.txt

frappe.ui.form.on("Customer Balance Comparison", {
  get_balance: function(frm, cdt, cdn) {
    if ( frappe.datetime.get_day_diff(frm.doc.compared_up_to, frm.doc.from_date) < 0){
      frm.doc.compared_up_to = null;
      frm.doc.from_date = null;
      frm.refresh_field('compared_up_to');
      frm.refresh_field('from_date');
      frappe.throw('From date should be equal or before than compared up to date')
    }
    frm
      .call({
        method: "erpnext.accounts.utils.get_balance_on",
        args: {
          date: frm.doc.compared_up_to,
          party_type: "Customer",
          party: frm.doc.customer,
          company: frm.doc.company
        }
      })
      .then(r => {
        frappe.model.set_value(cdt, cdn, "our_balance", r.message);
        frm.trigger("their_balance");
      })
      .then(r => {
        frm.call("get_ledger").then(r => {
          if (r.message) {
            let result = r.message
            frm.doc.details = null
            if (frappe.datetime.get_day_diff(frm.doc.compared_up_to, result[i].posting_date) >=0){
              console.log(frappe.datetime.get_day_diff(frm.doc.compared_up_to, result[i].posting_date), 'difference')
              frm.add_child('details', {
                date : result[i].posting_date,
                debit : result[i].debit,
                credit : result[i].credit,
                document_type : result[i].voucher_type,
                voucher : result[i].voucher_no,
                matched : 1
              })
            }
            frm.refresh_field('details')
          }
        });
      });
  },

  customer: function(frm) {
    if (frm.doc.customer) {
      if (frm.doc.from_date && frm.doc.compared_up_to) {
        frm.trigger("get_balance");
      }
    } else {
      frm.doc.our_balance = 0;
      frm.refresh_field("our_balance");
      frm.trigger("their_balance");
    }
  },

  from_date: function(frm) {
    if (frm.doc.from_date) {
      if (frm.doc.compared_up_to && frm.doc.customer) {
        frm.trigger("get_balance");
      }
    } else {
      frm.doc.our_balance = 0;
      frm.refresh_field("our_balance");
      frm.trigger("their_balance");
    }
  },

  compared_up_to: function(frm) {
    if (frm.doc.compared_up_to) {
      if (frm.doc.from_date && frm.doc.customer) {
        frm.trigger("get_balance");
      }
    } else {
      frm.doc.our_balance = 0;
      frm.refresh_field("our_balance");
      frm.trigger("their_balance");
    }
  },
  our_balance: function(frm) {
    let doc = frm.doc;
    if (doc.their_balance != null || doc.their_balance != "") {
      if (doc.our_balance == doc.their_balance) {
        doc.balance_status = "Matched";
      } else {
        doc.balance_status = "Not Matched";
      }
      frm.refresh_field("balance_status");
    }
  },
  their_balance: function(frm) {
    let doc = frm.doc;
    if (doc.our_balance != null || doc.our_balance != "") {
      if (doc.our_balance == doc.their_balance) {
        doc.balance_status = "Matched";
      } else {
        doc.balance_status = "Not Matched";
      }
      frm.refresh_field("balance_status");
      if (doc.our_balance != null && doc.their_balance != null) {
        doc.balance_difference = doc.our_balance - doc.their_balance;
        frm.refresh_field("balance_difference");
      }
    }
  }
});

frappe.ui.form.on('Customer Balance Comparison Details', {
  matched: function(frm, cdt, cdn){
    let row = frappe.get_doc(cdt, cdn)
    if ( row.matched == 1){
      frappe.model.set_value(cdt, cdn, 'differ', 0)
    }
    else {
      frappe.model.set_value(cdt, cdn, 'differ', 1)
    }
  },

  differ: function(frm, cdt, cdn){
    let row = frappe.get_doc(cdt, cdn)
    if ( row.differ == 1){
      frappe.model.set_value(cdt, cdn, 'matched', 0)
    }
    else {
      frappe.model.set_value(cdt, cdn, 'matched', 1)
    }
  }
})