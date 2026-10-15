from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
)

from database import (
    initialize_database,
    save_ticket,
    get_all_tickets,
    update_ticket_status,
    move_ticket_to_spam,
    move_ticket_to_trash,
    restore_ticket,
)

from ai_service import generate_mock_response


app = Flask(__name__)

initialize_database()


@app.route("/")
def home():
    search = request.args.get("search", "").strip()
    status = request.args.get("status", "").strip() or None
    view = request.args.get("view", "all").strip()

    valid_statuses = {"Open", "Pending", "Closed"}
    valid_views = {"all", "spam", "trash"}

    if status not in valid_statuses:
        status = None

    if view not in valid_views:
        view = "all"

    tickets = get_all_tickets(
        search=search,
        status=status,
        view=view,
    )

    return render_template(
        "index.html",
        tickets=tickets,
        search=search,
        status=status or "",
        view=view,
        message=request.args.get("message"),
        category=request.args.get("category"),
        priority=request.args.get("priority"),
        summary=request.args.get("summary"),
        suggested_response=request.args.get("suggested_response"),
        error=request.args.get("error"),
    )


@app.route("/classify", methods=["POST"])
def classify():
    message = request.form.get("message", "")

    try:
        result = generate_mock_response(message)

        save_ticket(
            message.strip(),
            result["category"],
            result["priority"],
        )

        return redirect(
            url_for(
                "home",
                message=message.strip(),
                category=result["category"],
                priority=result["priority"],
                summary=result["summary"],
                suggested_response=result["suggested_response"],
            )
        )

    except (TypeError, ValueError) as error:
        tickets = get_all_tickets()

        return render_template(
            "index.html",
            tickets=tickets,
            message=message,
            error=str(error),
        ), 400


@app.route("/tickets/<int:ticket_id>/status", methods=["POST"])
def change_ticket_status(ticket_id):
    status = request.form.get("status", "")
    return_to = request.form.get("return_to", "/")

    try:
        updated = update_ticket_status(ticket_id, status)
    except ValueError:
        return redirect(
            url_for("home", error="Invalid ticket status.")
        )

    if not updated:
        return redirect(
            url_for("home", error="Ticket could not be updated.")
        )

    safe_return_to = (
        return_to
        if return_to.startswith("/") and not return_to.startswith("//")
        else url_for("home")
    )

    return redirect(safe_return_to)


@app.route("/tickets/<int:ticket_id>/spam", methods=["POST"])
def mark_ticket_spam(ticket_id):
    move_ticket_to_spam(ticket_id)
    return redirect(url_for("home", view="spam"))


@app.route("/tickets/<int:ticket_id>/trash", methods=["POST"])
def trash_ticket(ticket_id):
    move_ticket_to_trash(ticket_id)
    return redirect(url_for("home", view="trash"))


@app.route("/tickets/<int:ticket_id>/restore", methods=["POST"])
def restore_trashed_ticket(ticket_id):
    restore_ticket(ticket_id)
    return redirect(url_for("home"))

# TEMPORARY: Reset only the ticket ID counter.
@app.route("/temporary-reset-ticket-counter", methods=["POST"])
def temporary_reset_ticket_counter():
    expected_token = os.environ.get("DEMO_RESET_TOKEN", "")
    provided_token = request.form.get("token", "")

    if not expected_token or not secrets.compare_digest(
        provided_token, expected_token
    ):
        abort(404)

    connection = sqlite3.connect(DATABASE_NAME)

    try:
        connection.execute(
            "DELETE FROM sqlite_sequence WHERE name = ?",
            ("tickets",)
        )
        connection.commit()
    finally:
        connection.close()

    return "Ticket ID counter reset. Existing tickets were not deleted."

if __name__ == "__main__":
    app.run(debug=True)
