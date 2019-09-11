import frappe
from frappe.utils import flt, get_datetime, getdate, add_days, date_diff, nowdate, today
from frappe.model.document import Document

def update_customer(self,cdt):
    if self.party_type == 'Customer'
        customer = frappe.get_doc('Customer',self.party)
        customer.db_set('last_payment_date',self.posting_date)
        customer.db_set('last_payment_amount',self.paid_amount)
