import sqlite3


DATABASE_NAME = "tickets.db"


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


def get_all_tickets():
    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            SELECT id, message, category, priority, created_at
            FROM tickets
            ORDER BY id DESC
            """
        )

        return [dict(row) for row in cursor.fetchall()]

    finally:
        connection.close()
