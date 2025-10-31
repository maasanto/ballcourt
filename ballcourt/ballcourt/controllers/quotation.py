import frappe
from frappe import _
from frappe.utils import get_datetime, now_datetime


def enforce_booking_notice(quotation, method):
	"""
	Enforces that customers can only book within their allowed advance booking window.
	Raises an exception if the booking is too far in advance.
	"""
	permitted_notice_seconds = get_permitted_notice(quotation.customer)

	if not permitted_notice_seconds:
		return

	if not quotation.items:
		return

	if not quotation.items[-1].item_booking:
		return

	booking_notice_seconds = calculate_booking_notice(frappe.get_doc("Item Booking", quotation.items[-1].item_booking))

	if booking_notice_seconds > permitted_notice_seconds:
		message = format_duration_message(booking_notice_seconds, permitted_notice_seconds)
		frappe.throw(
			message,
			title=_("Booking Too Far in Advance")
		)

def calculate_booking_notice(item_booking):
	"""
	Calculates the number of seconds between now and the earliest booking item date.
	Returns the notice in seconds (integer).
	"""
	if not item_booking:
		return 0

	# Get the start datetime and current datetime
	start_datetime = get_datetime(item_booking.starts_on)
	current_datetime = now_datetime()

	# Calculate difference in seconds
	time_difference = (start_datetime - current_datetime).total_seconds()

	# Return the number of seconds (minimum 0 if booking is in the past)
	return max(0, int(time_difference))

def get_permitted_notice(customer):
	"""
	Retrieves the permitted booking notice (in seconds) for a customer.
	Returns None if not set, or the number of seconds as an integer.
	"""
	if not customer:
		return None

	customer_group = frappe.db.get_value("Customer", customer, "customer_group")
	permitted_notice = frappe.db.get_value("Customer Group", customer_group, "custom_permitted_booking_notice")

	if permitted_notice is None:
		return None

	# Duration fields return seconds, ensure we return an integer
	try:
		return int(permitted_notice)
	except (ValueError, TypeError):
		return None

def format_duration_message(booking_seconds, permitted_seconds):
	"""
	Formats a complete error message about booking notice.
	The format is determined by the permitted_seconds value:
	- If permitted is in full days (no hours), show days only
	- If permitted is in hours only (no days), show hours only
	- If permitted has both days and hours, show both
	"""
	# Calculate booking duration components
	booking_days = booking_seconds // 86400
	booking_remaining = booking_seconds % 86400
	booking_hours = booking_remaining // 3600

	# Calculate permitted duration components
	permitted_days = permitted_seconds // 86400
	permitted_remaining = permitted_seconds % 86400
	permitted_hours = permitted_remaining // 3600

	if permitted_days > 0:
		if booking_days > 0 and booking_hours > 0:
			booking_msg = _("{0} days and {1} hours").format(booking_days, booking_hours)
		elif booking_days > 0:
			booking_msg = _("{0} days and 0 hours").format(booking_days)
		else:
			booking_msg = _("0 days and {0} hours").format(booking_hours)
		if permitted_hours > 0:
			permitted_msg = _("{0} days and {1} hours").format(permitted_days, permitted_hours)
		else:
			permitted_msg = _("{0} days").format(permitted_days, permitted_hours)

	# If permitted is hours only, show hours only
	else:
		booking_total_hours = int(booking_seconds / 3600)
		permitted_total_hours = int(permitted_seconds / 3600)
		booking_msg = _("{0} hours").format(booking_total_hours)
		permitted_msg = _("{0} hours").format(permitted_total_hours)

	return _("This booking is {0} in advance, but your tier only allows bookings up to {1} in advance.").format(booking_msg, permitted_msg)
