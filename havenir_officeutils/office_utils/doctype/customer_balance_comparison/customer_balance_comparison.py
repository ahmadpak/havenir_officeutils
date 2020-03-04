# -*- coding: utf-8 -*-
# Copyright (c) 2019, Havenir and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class CustomerBalanceComparison(Document):
    def validate(self):
        if self.our_balance != self.their_balance:
            self.balance_status = 'Not Matched'
        else:
            self.balance_status = 'Matched'
        if self.our_balance != None and self.their_balance != None:
            self.balance_difference = self.our_balance - self.their_balance
    def on_submit(self):
        sup = frappe.get_doc('Customer', '{0}'.format(self.customer))
        sup.db_set('last_balance_comparison_date', self.compared_up_to)
        remaining_invoices = frappe.db.get_list('Sales Invoice',
                                                filters={
                                                    'posting_date': ['>', self.compared_up_to],
                                                    'customer': self.customer
                                                },
                                                fields=['name'])
        remaining_payments = frappe.db.get_list('Payment Entry',
                                                filters={
                                                    'posting_date': ['>', self.compared_up_to],
                                                    'party_type': 'Customer',
                                                    'party': self.customer
                                                })
        
        if (remaining_invoices or remaining_payments) and self.our_balance == self.their_balance:
            sup.db_set('balance_matched', 'Matched till last comparison date')
        else:
            if self.our_balance == self.their_balance:
                sup.db_set('balance_matched', 'Matched')
            else:
                sup.db_set('balance_matched', 'Not Matched')
        update_docs(self)
    
    def get_ledger(self):
        # frappe.utils.data.add_days(self.from_date, -1)
        result = frappe.get_list('GL Entry', filters = {
            'account': ['like', '%Debtors%'],
            'party': self.customer,
            'docstatus': 1,
            'posting_date': ['between', self.from_date, 'and', self.compared_up_to]
        }, fields = [
            'posting_date',
            'debit',
            'credit',
            'voucher_type',
            'voucher_no'
        ], order_by = 'posting_date asc', page_length = 2000000)
        return result
        

def update_docs(self):
    for row in self.details:
        doc = frappe.get_doc(row.document_type, row.voucher)
        if row.matched == 1:
            doc.db_set('reconciled', 'Matched')
        else:
            doc.db_set('reconciled', 'Differ')
        doc.db_set('reconciled_by', frappe.session.user)
        doc.save()
        doc.submit()