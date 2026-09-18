import frappe.www.login as core_login

no_cache = core_login.no_cache


def get_context(context):
	return core_login.get_context(context)
