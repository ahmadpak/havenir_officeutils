from __future__ import unicode_literals
import frappe
from frappe import _


def get_data():
    return[
        {
            "label": ("Customer Utils"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Payment Recovery Calls",
                    "label": _("Payment Recovery Calls"),
                    "description": _("Calls to customer for payment recovery."),
                    "onboard": 1,
                },
            ]
        },
        {
            "label": ("Supplier Utils"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Supplier Balance Comparison",
                    "label": _("Supplier Balance Comparison"),
                    "description": _("Balance comparison with suppliers."),
                    "onboard": 1,
                },
            ]
        }
    ]
