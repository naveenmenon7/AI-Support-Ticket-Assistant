import os
import tempfile
import unittest

import database


class TestTicketDatabase(unittest.TestCase):

    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.close()

        self.original_database_name = database.DATABASE_NAME
        database.DATABASE_NAME = self.temp_file.name

        database.initialize_database()

        self.ticket_id = database.save_ticket(
            "I was charged twice for my subscription.",
            "Billing",
            "High"
        )

        self.other_ticket_id = database.save_ticket(
            "I forgot my password.",
            "Account Access",
            "Medium"
        )

    def tearDown(self):
        database.DATABASE_NAME = self.original_database_name
        os.unlink(self.temp_file.name)

    def test_new_ticket_defaults_to_open(self):
        tickets = database.get_all_tickets()
        self.assertEqual(tickets[0]["status"], "Open")

    def test_search_finds_matching_ticket(self):
        tickets = database.get_all_tickets(search="charged")
        self.assertEqual(len(tickets), 1)
        self.assertEqual(tickets[0]["id"], self.ticket_id)

    def test_status_filter_returns_matching_tickets(self):
        database.update_ticket_status(self.ticket_id, "Pending")

        tickets = database.get_all_tickets(status="Pending")

        self.assertEqual(len(tickets), 1)
        self.assertEqual(tickets[0]["id"], self.ticket_id)

    def test_invalid_status_is_rejected(self):
        with self.assertRaises(ValueError):
            database.update_ticket_status(self.ticket_id, "Urgent")

    def test_ticket_can_be_marked_as_spam(self):
        database.move_ticket_to_spam(self.ticket_id)

        self.assertNotIn(
            self.ticket_id,
            [ticket["id"] for ticket in database.get_all_tickets()]
        )

        spam_tickets = database.get_all_tickets(view="spam")
        self.assertEqual(len(spam_tickets), 1)
        self.assertEqual(spam_tickets[0]["id"], self.ticket_id)

    def test_ticket_can_be_trashed(self):
        database.move_ticket_to_trash(self.ticket_id)

        self.assertEqual(
            len(database.get_all_tickets(view="all")), 1
        )
        self.assertEqual(
            len(database.get_all_tickets(view="trash")), 1
        )

    def test_trashed_ticket_can_be_restored(self):
        database.move_ticket_to_trash(self.ticket_id)

        self.assertTrue(database.restore_ticket(self.ticket_id))

        tickets = database.get_all_tickets(view="all")
        self.assertEqual(len(tickets), 2)

    def test_invalid_view_is_rejected(self):
        with self.assertRaises(ValueError):
            database.get_all_tickets(view="unknown")


if __name__ == "__main__":
    unittest.main()
