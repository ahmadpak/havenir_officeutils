# -*- coding: utf-8 -*-
# Copyright (c) 2019, Havenir and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class PaymentRecoveryCalls(Document):
	def validate(self):
		pass

	def on_submit(self):
		self.update_customer_rating()
		self.create_event()
	
	def update_customer_rating(self):
		for row in self.call_details:
			customer = frappe.get_doc('Customer',row.customer)
			if row.rating == 5:
				new_stars = customer.five_stars + 1
				customer.db_set('five_stars',new_stars)
			elif row.rating == 4:
				new_stars = customer.four_stars + 1
				customer.db_set('four_stars',new_stars)
			elif row.rating == 3:
				new_stars = customer.three_stars + 1
				customer.db_set('three_stars',new_stars)
			elif row.rating == 2:
				new_stars = customer.two_stars + 1
				customer.db_set('two_stars',new_stars)
			elif row.rating == 1:
				new_stars = customer.one_star + 1
				customer.db_set('one_star',new_stars)
			average_stars = 5*customer.five_stars + 4*customer.four_stars + 3*customer.three_stars + 2*customer.two_stars + 1*customer.one_star
			average_stars = average_stars/(customer.five_stars+customer.four_stars+customer.three_stars+customer.two_stars+customer.one_star)
			customer.db_set('rating',average_stars)
			customer.db_set('next_due_date',row.next_due_date)
			customer.db_set('time',row.time)

	def create_event(self):
		for row in self.call_details:
			new_event = frappe.new_doc('Event')
			subject = 'Call ' + row.customer
			datetime = str(row.next_due_date) + ' ' + str(row.time) 
			new_event.update({
				'subject': subject,
				'event_category': 'Call',
				'color': '#ffc4c4',
				'starts_on': datetime,
				'description': row.remarks
			})
			new_event.save()

@frappe.whitelist()
def get_last_paid_amount(customer):
	customer_doc = frappe.get_doc('Customer',customer)
	return {'last_payment_date':customer_doc.last_payment_date,'last_payment_amount':customer_doc.last_payment_amount,'rating':customer_doc.rating}