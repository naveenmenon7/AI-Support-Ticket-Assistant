from flask import Flask, render_template, request, redirect, url_for
from main import categorize_ticket, determine_priority
from database import initialize_database, save_ticket, get_all_tickets

app = Flask(__name__)

initialize_database()



@app.route("/")
def home():
    tickets = get_all_tickets()

    return render_template(
        "index.html",
        tickets=tickets,
        message=request.args.get("message"),
        category=request.args.get("category"),
        priority=request.args.get("priority")
    )




@app.route("/classify", methods=["POST"])
def classify():
    message = request.form.get("message", "")

    try:
        category = categorize_ticket(message)
        priority = determine_priority(message)

        save_ticket(message.strip(), category, priority)

        return redirect(
            url_for(
                "home",
                message=message.strip(),
                category=category,
                priority=priority
            )
        )

    except (TypeError, ValueError) as error:
        tickets = get_all_tickets()

        return render_template(
            "index.html",
            message=message,
            error=str(error),
            tickets=tickets
        ), 400



if __name__ == "__main__":
    app.run(debug=True)
