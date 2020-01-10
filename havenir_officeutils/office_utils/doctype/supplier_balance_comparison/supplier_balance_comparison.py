# -*- coding: utf-8 -*-
# Copyright (c) 2019, Havenir and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class SupplierBalanceComparison(Document):
    def on_submit(self):
        sup = frappe.get_doc('Supplier', '{0}'.format(self.supplier))
        sup.db_set('last_balance_comparison_date', self.compared_up_to)
        remaining_invoices = frappe.db.get_list('Purchase Invoice',
                                                filters={
                                                    'posting_date': ['>', self.compared_up_to],
                                                    'supplier': self.supplier
                                                },
                                                fields=['name'])
        remaining_payments = frappe.db.get_list('Payment Entry',
                                                filters={
                                                    'posting_date': ['>', self.compared_up_to],
                                                    'party_type': 'Supplier',
                                                    'party': self.supplier
                                                })
        
        if (remaining_invoices or remaining_payments) and self.our_balance == self.their_balance:
            sup.db_set('balance_matched', 'Matched till last comparison date')
        else:
            if self.our_balance == self.their_balance:
                sup.db_set('balance_matched', 'Matched')
            else:
                sup.db_set('balance_matched', 'Not Matched')
