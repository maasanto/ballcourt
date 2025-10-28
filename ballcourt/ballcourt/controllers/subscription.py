import frappe
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
				if plan == "Or":
					customer.customer_group = "Or"
				if plan == "Or+":
					customer.customer_group = "Or+"
				if plan == "Ligue":
					customer.customer_group = "Ligue"
				frappe.msgprint("Customer group updated to " + customer.customer_group)
			elif self.status == "Cancelled":
				customer.customer_group = "Argent"
				frappe.msgprint("Customer group updated to " + customer.customer_group)

			customer.save()
