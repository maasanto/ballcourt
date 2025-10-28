app_name = "ballcourt"
app_title = "Ballcourt"
app_publisher = "Antoine Maas"
app_description = "Opensource racquet sports club management"
app_email = "antoine.maas@amingenierie-opensource.fr"
app_license = "gpl-3.0"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "ballcourt",
# 		"logo": "/assets/ballcourt/logo.png",
# 		"title": "Ballcourt",
# 		"route": "/ballcourt",
# 		"has_permission": "ballcourt.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ballcourt/css/ballcourt.css"
# app_include_js = "/assets/ballcourt/js/ballcourt.js"

# include js, css files in header of web template
# web_include_css = "/assets/ballcourt/css/ballcourt.css"
# web_include_js = "/assets/ballcourt/js/ballcourt.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ballcourt/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}
# doctype_timeline_js = {"doctype" : "public/js/doctype_timeline.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "ballcourt/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "ballcourt.utils.jinja_methods",
# 	"filters": "ballcourt.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "ballcourt.install.before_install"
# after_install = "ballcourt.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ballcourt.uninstall.before_uninstall"
# after_uninstall = "ballcourt.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "ballcourt.utils.before_app_install"
# after_app_install = "ballcourt.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "ballcourt.utils.before_app_uninstall"
# after_app_uninstall = "ballcourt.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ballcourt.notifications.get_notification_config"

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

doc_events = {
	"Quotation": {
		"before_save": "ballcourt.ballcourt.controllers.quotation.enforce_booking_notice",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ballcourt.tasks.all"
# 	],
# 	"daily": [
# 		"ballcourt.tasks.daily"
# 	],
# 	"hourly": [
# 		"ballcourt.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ballcourt.tasks.weekly"
# 	],
# 	"monthly": [
# 		"ballcourt.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "ballcourt.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
extend_doctype_class = {
	"Subscription": "ballcourt.ballcourt.controllers.subscription.BallcourtSubscription",
}

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ballcourt.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "ballcourt.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["ballcourt.utils.before_request"]
# after_request = ["ballcourt.utils.after_request"]
# Job Events
# ----------
# before_job = ["ballcourt.utils.before_job"]
# after_job = ["ballcourt.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"ballcourt.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

