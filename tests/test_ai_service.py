import json
import unittest
from unittest.mock import Mock

from ai_service import validate_ai_response
from ai_service import generate_mock_response


class TestAIService(unittest.TestCase):

    def setUp(self):
        self.valid_response = {
            "category": "Billing",
            "priority": "High",
            "summary": "The customer was charged twice.",
            "suggested_response": (
                "We're sorry about the duplicate charge. "
                "Our team will investigate this issue."
            ),
        }

    def test_valid_response_is_parsed(self):
        response_text = json.dumps(self.valid_response)

        result = validate_ai_response(response_text)

        self.assertEqual(result["category"], "Billing")
        self.assertEqual(result["priority"], "High")
        self.assertEqual(
            result["summary"],
            "The customer was charged twice."
        )

    def test_whitespace_is_removed_from_text_fields(self):
        response = self.valid_response.copy()
        response["summary"] = "  Duplicate charge.  "

        result = validate_ai_response(json.dumps(response))

        self.assertEqual(result["summary"], "Duplicate charge.")

    def test_empty_response_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_ai_response("   ")

    def test_invalid_json_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_ai_response("not valid json")

    def test_missing_field_is_rejected(self):
        response = self.valid_response.copy()
        del response["summary"]

        with self.assertRaises(ValueError):
            validate_ai_response(json.dumps(response))

    def test_invalid_category_is_rejected(self):
        response = self.valid_response.copy()
        response["category"] = "Unrecognized Category"

        with self.assertRaises(ValueError):
            validate_ai_response(json.dumps(response))

    def test_invalid_priority_is_rejected(self):
        response = self.valid_response.copy()
        response["priority"] = "Critical"

        with self.assertRaises(ValueError):
            validate_ai_response(json.dumps(response))

    def test_empty_suggested_response_is_rejected(self):
        response = self.valid_response.copy()
        response["suggested_response"] = "  "

        with self.assertRaises(ValueError):
            validate_ai_response(json.dumps(response))

    def test_non_string_input_is_rejected(self):
        with self.assertRaises(TypeError):
            validate_ai_response(None)

    def test_mocked_ai_response(self):
        # Simulates an AI client returning a response.
        # No real AI client or API request is used.
        mock_client = Mock()
        mock_client.generate.return_value = json.dumps(
            self.valid_response
        )

        raw_response = mock_client.generate("Example support ticket")
        result = validate_ai_response(raw_response)

        self.assertEqual(result["category"], "Billing")
        mock_client.generate.assert_called_once_with(
            "Example support ticket"
        )
    
    def test_mock_response_uses_existing_classifier(self):
        result = generate_mock_response(
            "I was charged twice."
        )

        self.assertEqual(result["category"], "Billing")
        self.assertEqual(result["priority"], "High")
        self.assertTrue(result["suggested_response"])

    def test_mock_response_rejects_empty_message(self):
        with self.assertRaises(ValueError):
            generate_mock_response("   ")

    def test_mock_response_rejects_non_string_message(self):
        with self.assertRaises(TypeError):
            generate_mock_response(None)



if __name__ == "__main__":
    unittest.main()
