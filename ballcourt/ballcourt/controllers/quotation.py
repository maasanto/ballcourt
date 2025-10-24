import frappe
from frappe import _
from frappe.utils import date_diff, get_datetime, now_datetime


def enforce_booking_notice(quotation, method):
	"""
	Enforces that customers can only book within their allowed advance booking window.
	Raises an exception if the booking is too far in advance.
	"""
	permitted_notice_days = get_permitted_notice(quotation.customer)

	if not permitted_notice_days:
		return

	if not quotation.items:
		return

	booking_notice_days = calculate_booking_notice(frappe.get_doc("Resource Booking", quotation.items[-1].item_booking))

	if booking_notice_days > permitted_notice_days:
		frappe.throw(
			_(f"This booking is {booking_notice_days} days in advance, but your tier only allows bookings up to {permitted_notice_days} days in advance."),
			title=_("Booking Too Far in Advance")
		)

def calculate_booking_notice(resource_booking):
	"""
	Calculates the number of days between now and the earliest booking item date.
	Returns the notice in days (integer).
	"""
	if not resource_booking:
		return 0

	# Calculate difference in days
	days_difference = date_diff(resource_booking.starts_on, now_datetime())

	# Return the number of days (minimum 0 if booking is in the past/same day)
	return max(0, days_difference)

def get_permitted_notice(customer):
	"""
	Retrieves the permitted booking notice (in days) for a customer.
	Returns None if not set, or the number of days as an integer.
	"""
	if not customer:
		return None

	customer_group = frappe.db.get_value("Customer", customer, "customer_group")
	permitted_notice = frappe.db.get_value("Customer Group", customer_group, "custom_permitted_booking_notice")

	if permitted_notice is None:
		return None

	# Ensure we return an integer
	try:
		return int(permitted_notice)
	except (ValueError, TypeError):
		return None
