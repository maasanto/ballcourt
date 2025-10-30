import frappe
from frappe import _
from erpnext.accounts.doctype.subscription.subscription import Subscription

class BallcourtSubscription(Subscription):

	def before_insert(self):
		# Vérifier que le client n'a pas déjà un badge
		customer = frappe.get_doc("Customer", self.customer)

		if customer.has_active_subscription():
			frappe.throw("Veuillez annuler l'abonnement en cours avant d'en démarrer un nouveau")

	def process(self):
		super().process()
		self.update_customer_group()

	def update_customer_group(self):
		if self.has_value_changed("status"):
			customer = frappe.get_doc("Customer", self.customer)
			if self.status not in ["Cancelled", "Pending"]:
				plan = self.plans[0].item
				if plan == "Badge Or":
					customer.customer_group = "Or"
				if plan == "Badge Or+":
					customer.customer_group = "Or+"
				if plan == "Badge Ligue":
					customer.customer_group = "Ligue"
			elif self.status == "Cancelled":
				customer.customer_group = "Argent"
			frappe.msgprint(_("Customer group updated to {0}").format(customer.customer_group))

			customer.save()
