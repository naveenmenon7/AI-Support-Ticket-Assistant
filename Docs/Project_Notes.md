# Support Desk — Project Notes

## Overview

Support Desk is a local Flask application for entering and managing customer support messages. It uses rule-based logic to categorize incoming messages and assign a priority, saves tickets to SQLite, and provides a browser-based ticket workspace.

## Architecture

- `app.py` — Flask application, page rendering, and request routes.
- `main.py` — message validation, category rules, and priority rules.
- `ai_service.py` — mock analysis response and response-structure validation.
- `database.py` — SQLite initialization and ticket CRUD/state operations.
- `templates/index.html` — page structure and interactive controls.
- `static/style.css` — layout, responsive styling, theme variables, accent palettes.
- `static/theme.js` — appearance selection behavior.
- `tests/` — automated tests for the app's key logic and behavior.

## Request Flow

1. A user enters a customer message through the New Ticket dialog.
2. The Flask route passes the message to the analysis service.
3. The current mock service uses the app's rule-based classifier and priority detector and returns a validated dictionary.
4. The ticket's message, category, and priority are saved to the SQLite database.
5. The browser displays the ticket list and the latest analysis result.
6. Users can search, filter, sort, update status, or move tickets to Spam or Trash and restore them.

## Classification Rules

Current classification is based on predefined keywords and phrases. It is not a trained machine-learning model and does not provide semantic understanding. Priority detection also uses phrase matching with a basic negation check, so edge cases may be misclassified.

## Mock Analysis Service

The analysis service returns a structured response containing category, priority, summary, and suggested response. The summary and suggested response are mock/template output. No live external AI API is called by the current version.

## Local Development

Install requirements:

```powershell
python -m pip install -r requirements.txt
```

Run the web app:

```powershell
python app.py
```

Run tests:

```powershell
python -m unittest discover -s tests -v
```

## Verification Checklist

Before a release or portfolio update:

- [ ] Run the full automated test suite and record the actual passed count.
- [ ] Create a ticket and check that it remains after reloading the page.
- [ ] Verify search and status filters.
- [ ] Verify sorting for ID, Category, Priority, Created, and Status.
- [ ] Verify Update, Spam, Trash, and Restore.
- [ ] Check light, dark, and system appearance.
- [ ] Check all accent colours.
- [ ] Check desktop and narrow mobile layouts.
- [ ] Confirm `.env`, `tickets.db`, `.venv`, and other local-only files are not staged for Git.

## Known Limitations

- No authentication or user roles.
- No production deployment configuration.
- No live model inference; AI responses are mocked.
- Keyword-based classification can miss context and multi-issue messages.
- SQLite is appropriate for a small local project; additional concurrency and deployment needs would require review.
