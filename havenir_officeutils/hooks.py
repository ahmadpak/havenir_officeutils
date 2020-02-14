# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "havenir_officeutils"
app_title = "Office Utils"
app_publisher = "Havenir"
app_description = "Doctypes for inhancing day to day reporting"
app_icon = "octicon octicon-file-graph"
app_color = "grey"
app_email = "info@havenir.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/havenir_officeutils/css/havenir_officeutils.css"
# app_include_js = "/assets/havenir_officeutils/js/havenir_officeutils.js"

# include js, css files in header of web template
# web_include_css = "/assets/havenir_officeutils/css/havenir_officeutils.css"
# web_include_js = "/assets/havenir_officeutils/js/havenir_officeutils.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "havenir_officeutils.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "havenir_officeutils.install.before_install"
# after_install = "havenir_officeutils.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "havenir_officeutils.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

fixtures = [{
    'dt': 'Custom Field', 'filters':[
        ['name','in',[
            'Customer-last_payment_amount',
            'Customer-last_payment_date',
            'Customer-five_stars',
            'Customer-four_stars',
            'Customer-three_stars',
            'Customer-two_stars',
            'Customer-one_star',
            'Customer-rating',
            'Customer-next_due_date',
            'Customer-time',
            'Customer-section_break_43',
            'Customer-column_break_43',
            'Purchase Invoice-reconciled',
            'Payment Entry-reconciled',
            'Journal Entry-reconciled',
            'Payment Entry-reconciled_by',
            'Journal Entry-reconciled_by',
            'Purchase Invoice-reconciled_by',
            'Sales Invoice-reconciled',
            'Sales Invoice-reconciled_by'
        ]]
    ]
}]

doc_events = {
    'Payment Entry':{
        'on_submit': 'havenir_officeutils.utils.payment_entry.update_customer'
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"havenir_officeutils.tasks.all"
# 	],
# 	"daily": [
# 		"havenir_officeutils.tasks.daily"
# 	],
# 	"hourly": [
# 		"havenir_officeutils.tasks.hourly"
# 	],
# 	"weekly": [
# 		"havenir_officeutils.tasks.weekly"
# 	]
# 	"monthly": [
# 		"havenir_officeutils.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "havenir_officeutils.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "havenir_officeutils.event.get_events"
# }

