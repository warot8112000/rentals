import frappe


@frappe.whitelist(allow_guest=True)
def get_test():
    return "Test API"


def throw_testHook(doc, event):
    """
    This function is a test hook that throws an exception.
    It is used to test the functionality of hooks in the application.
    """
    raise frappe.throw("Test Hook Event")


def get_query_conditions_for_vehicle(user):
    return "name = 1"
