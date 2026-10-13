import unittest

from main import categorize_ticket, determine_priority


class TestTicketClassification(unittest.TestCase):

    def test_billing_ticket(self):
        message = "I've been charged twice for my subscription."

        self.assertEqual(categorize_ticket(message), "Billing")
        self.assertEqual(determine_priority(message), "High")

    def test_account_access_ticket(self):
        message = "I forgot my password."

        self.assertEqual(
            categorize_ticket(message),
            "Account Access"
        )
        self.assertEqual(determine_priority(message), "Medium")

    def test_technical_support_ticket(self):
        message = "The application crashes when I open it."

        self.assertEqual(
            categorize_ticket(message),
            "Technical Support"
        )
        self.assertEqual(determine_priority(message), "High")

    def test_general_inquiry(self):
        message = "How do I change my profile picture?"

        self.assertEqual(
            categorize_ticket(message),
            "General Inquiry"
        )
        self.assertEqual(determine_priority(message), "Low")

    
    def test_empty_message_is_rejected(self):
        with self.assertRaises(ValueError):
            categorize_ticket("")

    def test_whitespace_message_is_rejected(self):
        with self.assertRaises(ValueError):
            categorize_ticket("   ")

    def test_non_string_message_is_rejected(self):
        with self.assertRaises(TypeError):
            categorize_ticket(None)



if __name__ == "__main__":
    unittest.main()