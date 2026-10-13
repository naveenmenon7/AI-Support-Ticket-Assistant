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


customer_message = input("Enter a customer support message: ")

category = categorize_ticket(customer_message)

print("Ticket Category:", category)
