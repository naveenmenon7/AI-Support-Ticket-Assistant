import os
import tempfile
import unittest

import app as app_module
import database


class TestSupportTicketApp(unittest.TestCase):

    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.close()

        self.original_database_name = database.DATABASE_NAME
        database.DATABASE_NAME = self.temp_file.name

        database.initialize_database()

        self.app = app_module.app
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def tearDown(self):
        database.DATABASE_NAME = self.original_database_name
        os.unlink(self.temp_file.name)

    def test_homepage_loads(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"AI Support Ticket Assistant",
            response.data
        )

    def test_valid_ticket_is_saved(self):
        response = self.client.post(
            "/classify",
            data={"message": "I was charged twice."}
        )

        self.assertEqual(response.status_code, 302)

        tickets = database.get_all_tickets()

        self.assertEqual(len(tickets), 1)
        self.assertEqual(tickets[0]["category"], "Billing")
        self.assertEqual(tickets[0]["priority"], "High")

    def test_refresh_does_not_resubmit_ticket(self):
        self.client.post(
            "/classify",
            data={"message": "I was charged twice."}
        )

        self.client.get("/")

        tickets = database.get_all_tickets()

        self.assertEqual(len(tickets), 1)

    def test_invalid_ticket_is_rejected(self):
        response = self.client.post(
            "/classify",
            data={"message": "   "}
        )

        self.assertEqual(response.status_code, 400)

        tickets = database.get_all_tickets()

        self.assertEqual(len(tickets), 0)

    def test_ticket_history_is_displayed(self):
        database.save_ticket(
            "I forgot my password.",
            "Account Access",
            "Medium"
        )

        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"I forgot my password.", response.data)
        self.assertIn(b"Account Access", response.data)


if __name__ == "__main__":
    unittest.main()
