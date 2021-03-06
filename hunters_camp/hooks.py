# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "hunters_camp"
app_title = "Hunters Camp"
app_publisher = "GNU"
app_description = "Property Management App"
app_icon = "octicon octicon-file-directory"
app_color = "#e67e22"
app_email = "contact@indictranstech.com"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/hunters_camp/css/hunters_camp.css"
# app_include_js = "/assets/hunters_camp/js/hunters_camp.js"

# include js, css files in header of web template
# web_include_css = "/assets/hunters_camp/css/hunters_camp.css"
# web_include_js = "/assets/hunters_camp/js/hunters_camp.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

fixtures = ["Custom Field"]
# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "hunters_camp.install.before_install"
# after_install = "hunters_camp.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "hunters_camp.notifications.get_notification_config"

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
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"hunters_camp.tasks.all"
# 	],
# 	"daily": [
# 		"hunters_camp.tasks.daily"
# 	],
# 	"hourly": [
# 		"hunters_camp.tasks.hourly"
# 	],
# 	"weekly": [
# 		"hunters_camp.tasks.weekly"
# 	]
# 	"monthly": [
# 		"hunters_camp.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "hunters_camp.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "hunters_camp.event.get_events"
# }

