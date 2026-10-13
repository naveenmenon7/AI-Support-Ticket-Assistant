def categorize_ticket(message):
    message = message.lower()

    if "refund" in message or "charged" in message or "payment" in message:
        return "Billing"

    elif "password" in message or "login" in message or "account" in message:
        return "Account Access"

    elif "error" in message or "bug" in message or "crash" in message:
        return "Technical Support"

    else:
        return "General Inquiry"


def determine_priority(message):
    message = message.lower()

    high_priority_keywords = [
        "charged twice",
        "payment failed",
        "crash",
        "not working",
        "urgent",
        "cannot access",
        ]

    for keyword in high_priority_keywords:
        if keyword in message:
            return "High"


    medium_priority_keywords = [
        "password",
        "login",
        "error",
        "refund",
    ]

    for keyword in medium_priority_keywords:
        if keyword in message:
            return "Medium"

    return "Low"

if __name__ == "__main__":
    customer_message = input("Enter a customer support message: ")

    category = categorize_ticket(customer_message)
    priority = determine_priority(customer_message)

    print("\n--- Ticket Details ---")
    print("Message:", customer_message)
    print("Category:", category)
    print("Priority:", priority)