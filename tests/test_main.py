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


    
    def test_negated_duplicate_charge_is_not_high(self):
        message = "I was not charged twice."

        self.assertNotEqual(
            determine_priority(message),
            "High"
        )

    def test_hacked_account_is_high_priority(self):
        message = "My account was hacked."

        self.assertEqual(
            determine_priority(message),
            "High"
        )

    def test_ordinary_payment_question_is_medium(self):
        message = "I have a question about my payment."

        self.assertEqual(
            determine_priority(message),
            "Medium"
        )


    
    def test_password_keyword_in_general_question(self):
        message = "What password manager do you recommend?"

        self.assertEqual(
            categorize_ticket(message),
            "Account Access"
        )
        self.assertEqual(determine_priority(message), "Medium")

    def test_message_with_multiple_issue_types(self):
        message = "I cannot log in and my payment failed."

        self.assertEqual(categorize_ticket(message), "Billing")
        self.assertEqual(determine_priority(message), "High")

    def test_application_not_working_is_high_priority(self):
        message = "The application is not working."

        self.assertEqual(determine_priority(message), "High")

    def test_negated_crash_is_not_high_priority(self):
        message = "The application is not crashing."

        self.assertNotEqual(
            determine_priority(message),
            "High"
        )




if __name__ == "__main__":
    unittest.main()