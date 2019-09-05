# -*- coding: utf-8 -*-
# Copyright (c) 2019, Havenir and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class PaymentRecoveryCalls(Document):
	pass

@frappe.whitelist()
def get_last_paid_amount(customer):
	customer_doc = frappe.get_doc('Customer',customer)
	return {'last_payment_date':customer_doc.last_payment_date,'last_payment_amount':customer_doc.last_payment_amount}