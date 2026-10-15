def validate_message(message):
    if not isinstance(message, str):
        raise TypeError("Message must be a string.")

    if not message.strip():
        raise ValueError("Message cannot be empty.")

    return message.strip()



def categorize_ticket(message):
    message = validate_message(message).lower()

    billing_keywords = ["refund", "charged", "payment"]
    account_keywords = ["password", "login", "account"]
    technical_keywords = ["error", "bug", "crash"]

    if any(keyword in message for keyword in billing_keywords):
        return "Billing"

    elif any(keyword in message for keyword in account_keywords):
        return "Account Access"

    elif any(keyword in message for keyword in technical_keywords):
        return "Technical Support"

    return "General Inquiry"





def determine_priority(message):
    message = validate_message(message).lower()

    high_priority_phrases = [
        "charged twice",
        "payment failed",
        "app crashes",
        "application crashes",
        "not working",
        "urgent",
        "cannot access",
        "unable to access",
        "account hacked",
        "account was hacked",
        "account compromised",
        "account was compromised",
    ]

    negations = ["not ", "never ", "no "]

    for phrase in high_priority_phrases:
        phrase_position = message.find(phrase)

        if phrase_position == -1:
            continue

        preceding_text = message[max(0, phrase_position - 10):phrase_position]

        if any(word in preceding_text for word in negations):
            continue

        return "High"

    medium_priority_keywords = [
        "password",
        "login",
        "error",
        "refund",
        "payment",
        "account",
    ]

    if any(keyword in message for keyword in medium_priority_keywords):
        return "Medium"

    return "Low"




if __name__ == "__main__":
    try:
        customer_message = input(
            "Enter a customer support message: "
        )

        category = categorize_ticket(customer_message)
        priority = determine_priority(customer_message)

        print("\n--- Ticket Details ---")
        print("Message:", customer_message)
        print("Category:", category)
        print("Priority:", priority)

    except (TypeError, ValueError) as error:
        print("Invalid input:", error)
