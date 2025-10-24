import frappe
from frappe import _
from frappe.utils import date_diff, get_datetime, now_datetime


def enforce_booking_notice(quotation, method):
	"""
	Enforces that customers can only book within their allowed advance booking window.
	Raises an exception if the booking is too far in advance.
	"""
	permitted_distance_days = get_permitted_distance(quotation.customer)

	if not permitted_distance_days:
		return

	if not quotation.items:
		return

	booking_distance_days = calculate_booking_distance(frappe.get_doc("Resource Booking", quotation.items[-1].item_booking))

	if booking_distance_days > permitted_distance_days:
		frappe.throw(
			_(f"This booking is {booking_distance_days} days in advance, but your tier only allows bookings up to {permitted_distance_days} days in advance."),
			title=_("Booking Too Far in Advance")
		)

def calculate_booking_distance(resource_booking):
	"""
	Calculates the number of days between now and the earliest booking item date.
	Returns the distance in days (integer).
	"""
	if not resource_booking:
		return 0

	# Calculate difference in days
	days_difference = date_diff(resource_booking.starts_on, now_datetime())

	# Return the number of days (minimum 0 if booking is in the past/same day)
	return max(0, days_difference)

def get_permitted_distance(customer):
	"""
	Retrieves the permitted booking distance (in days) for a customer.
	Returns None if not set, or the number of days as an integer.
	"""
	if not customer:
		return None

	customer_group = frappe.db.get_value("Customer", customer, "customer_group")
	permitted_notice = frappe.db.get_value("Customer Group", customer_group, "custom_permitted_booking_notice")

	if permitted_distance is None:
		return None

	# Ensure we return an integer
	try:
		return int(permitted_distance)
	except (ValueError, TypeError):
		return None
