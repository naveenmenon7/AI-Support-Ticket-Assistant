import sqlite3

DATABASE_NAME = "tickets.db"

VALID_STATUSES = {"Open", "Pending", "Closed"}
VALID_VIEWS = {"all", "spam", "trash"}


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_connection()

    try:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message TEXT NOT NULL,
                category TEXT NOT NULL,
                priority TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Safely upgrade databases created by earlier versions.
        columns = {
            row["name"]
            for row in connection.execute(
                "PRAGMA table_info(tickets)"
            ).fetchall()
        }

        if "status" not in columns:
            connection.execute("""
                ALTER TABLE tickets
                ADD COLUMN status TEXT NOT NULL DEFAULT 'Open'
            """)

        if "is_spam" not in columns:
            connection.execute("""
                ALTER TABLE tickets
                ADD COLUMN is_spam INTEGER NOT NULL DEFAULT 0
            """)

        if "is_trashed" not in columns:
            connection.execute("""
                ALTER TABLE tickets
                ADD COLUMN is_trashed INTEGER NOT NULL DEFAULT 0
            """)

        connection.commit()

    finally:
        connection.close()


def save_ticket(message, category, priority):
    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            INSERT INTO tickets (message, category, priority)
            VALUES (?, ?, ?)
            """,
            (message, category, priority)
        )

        connection.commit()
        return cursor.lastrowid

    finally:
        connection.close()


def get_all_tickets(search="", status=None, view="all"):
    if view not in VALID_VIEWS:
        raise ValueError("Invalid ticket view.")

    if status is not None and status not in VALID_STATUSES:
        raise ValueError("Invalid ticket status.")

    connection = get_connection()

    try:
        conditions = []
        parameters = []

        if view == "spam":
            conditions.append("is_spam = 1")
            conditions.append("is_trashed = 0")
        elif view == "trash":
            conditions.append("is_trashed = 1")
        else:
            conditions.append("is_spam = 0")
            conditions.append("is_trashed = 0")

        if status is not None:
            conditions.append("status = ?")
            parameters.append(status)

        if search.strip():
            conditions.append("message LIKE ?")
            parameters.append(f"%{search.strip()}%")

        query = """
            SELECT id, message, category, priority, created_at,
                   status, is_spam, is_trashed
            FROM tickets
            WHERE
        """ + " AND ".join(conditions) + """
            ORDER BY id DESC
        """

        cursor = connection.execute(query, parameters)
        return [dict(row) for row in cursor.fetchall()]

    finally:
        connection.close()


def update_ticket_status(ticket_id, status):
    if status not in VALID_STATUSES:
        raise ValueError("Invalid ticket status.")

    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            UPDATE tickets
            SET status = ?
            WHERE id = ? AND is_spam = 0 AND is_trashed = 0
            """,
            (status, ticket_id)
        )

        connection.commit()
        return cursor.rowcount > 0

    finally:
        connection.close()


def move_ticket_to_spam(ticket_id):
    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            UPDATE tickets
            SET is_spam = 1
            WHERE id = ? AND is_trashed = 0
            """,
            (ticket_id,)
        )

        connection.commit()
        return cursor.rowcount > 0

    finally:
        connection.close()


def move_ticket_to_trash(ticket_id):
    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            UPDATE tickets
            SET is_trashed = 1, is_spam = 0
            WHERE id = ?
            """,
            (ticket_id,)
        )

        connection.commit()
        return cursor.rowcount > 0

    finally:
        connection.close()


def restore_ticket(ticket_id):
    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            UPDATE tickets
            SET is_spam = 0, is_trashed = 0
            WHERE id = ?
            """,
            (ticket_id,)
        )

        connection.commit()
        return cursor.rowcount > 0

    finally:
        connection.close()
