import json


VALID_CATEGORIES = {
    "Billing",
    "Account Access",
    "Technical Support",
    "General Inquiry",
}

VALID_PRIORITIES = {"High", "Medium", "Low"}


def validate_ai_response(response_text):
    """Parse and validate a structured AI response without calling an AI API."""

    if not isinstance(response_text, str):
        raise TypeError("AI response must be a string.")

    if not response_text.strip():
        raise ValueError("AI response cannot be empty.")

    try:
        response = json.loads(response_text)
    except json.JSONDecodeError as error:
        raise ValueError("AI response must contain valid JSON.") from error

    if not isinstance(response, dict):
        raise ValueError("AI response must be a JSON object.")

    required_fields = {
        "category",
        "priority",
        "summary",
        "suggested_response",
    }

    if not required_fields.issubset(response.keys()):
        raise ValueError("AI response is missing required fields.")

    if response["category"] not in VALID_CATEGORIES:
        raise ValueError("AI response contains an invalid category.")

    if response["priority"] not in VALID_PRIORITIES:
        raise ValueError("AI response contains an invalid priority.")

    for field in ("summary", "suggested_response"):
        value = response[field]

        if not isinstance(value, str) or not value.strip():
            raise ValueError(
                f"AI response field '{field}' must be a non-empty string."
            )

    return {
        "category": response["category"],
        "priority": response["priority"],
        "summary": response["summary"].strip(),
        "suggested_response": response["suggested_response"].strip(),
    }


def generate_mock_response(message):
    """Return a deterministic mock response without using an AI model."""

    if not isinstance(message, str):
        raise TypeError("Message must be a string.")

    message = message.strip()

    if not message:
        raise ValueError("Message cannot be empty.")

    from main import categorize_ticket, determine_priority

    category = categorize_ticket(message)
    priority = determine_priority(message)

    response = {
        "category": category,
        "priority": priority,
        "summary": message[:200],
        "suggested_response": (
            "Thank you for contacting support. "
            "Your ticket has been recorded for review by our team."
        ),
    }

    return validate_ai_response(json.dumps(response))
