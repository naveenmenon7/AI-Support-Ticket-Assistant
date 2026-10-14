# NM's Support Desk — AI Support Ticket Assistant

A Flask-based customer support ticket management web application built with Python and SQLite. It classifies incoming support messages, assigns a priority, and provides a workspace for searching, sorting, and managing tickets.

The current version uses rule-based classification and a mock AI response service. It runs locally and does not require paid AI APIs.

## Features

### Ticket analysis
- Categorizes messages as **Billing**, **Account Access**, **Technical Support**, or **General Inquiry**.
- Assigns **High**, **Medium**, or **Low** priority using predefined phrases and rules.
- Validates input and rejects empty or invalid messages.
- Displays a summary and a suggested response from the mock response service.

### Ticket management
- Saves tickets to a local SQLite database.
- Searches ticket messages.
- Filters tickets by status: Open, Pending, or Closed.
- Sorts the ticket table by ID, category, priority, creation date, and status.
- Updates ticket status.
- Moves tickets to Spam or Trash and restores them.
- Preserves ticket data between application restarts.

### Interface
- Responsive workspace with desktop sidebar and mobile navigation.
- Light, dark, and system appearance options.
- Selectable accent colours: Aqua Blue, Pink, Yellow, and Red.
- Modal for submitting and analyzing a new ticket.

### Testing
- Automated tests using Python's built-in `unittest` framework.
- Tests cover classification logic, response validation, database operations, and Flask routes.

## Technology Stack

- **Python** — application logic and classification
- **Flask** — web application and routes
- **SQLite** — persistent ticket storage
- **HTML and CSS** — interface and responsive layout
- **JavaScript** — UI interactions such as sorting, theme/accent selection, and mobile navigation
- **unittest** — automated tests
- **Git and GitHub** — version control

## Project Structure

```text
AI-Support-Ticket-Assistant/
├── app.py
├── main.py
├── ai_service.py
├── database.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── theme.js
├── tests/
│   ├── test_main.py
│   ├── test_app.py
│   ├── test_ai_service.py
│   └── test_database.py
├── Docs/
│   └── Learning_Log.md
├── .gitignore
└── README.md
```

> Keep local database files and environment files out of Git. Make sure `.gitignore` excludes them before pushing.

## Getting Started

### Prerequisites

- Python 3 installed
- Git, if cloning the repository

### 1. Clone the repository

```bash
git clone https://github.com/naveenmenon7/AI-Support-Ticket-Assistant.git
cd AI-Support-Ticket-Assistant
```

### 2. Create and activate a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use the virtual environment's Python executable directly or activate it using your preferred terminal.

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the web application

```bash
python app.py
```

Open the local address printed by Flask in your browser (usually `http://127.0.0.1:5000`).

The SQLite database is initialized by the application when it starts.

### 5. Run the automated tests

Stop the development server if necessary, then run:

```bash
python -m unittest discover -s tests -v
```

The test suite previously had 43 passing tests during development. Run the command above to confirm the current result after your latest UI changes.

## Example Classification

Example customer message:

```text
I've been charged twice for my subscription.
```

The rule-based classifier is expected to categorize this message as **Billing** and assign **High** priority based on the matching rules.

## AI Integration Status

**The current release does not call a live AI model.**

The application uses predefined classification and priority rules, plus a mock response service that returns structured sample analysis such as a summary and suggested response. This keeps the project free to run and avoids external API costs.

The mock service demonstrates how an analysis service can be integrated and validated. Its summaries and suggested replies should not be represented as live model-generated output.

## Current Limitations

- Classification and priority rely on keyword and phrase matching, so context and nuanced wording may be missed.
- Messages containing multiple issues are not analyzed by a language model.
- The summary and suggested response are mocked templates rather than live AI-generated content.
- The current application is designed for local use; deployment, authentication, and multi-user access are outside the current scope.

## Future Improvements

- Optionally integrate a local language model, such as Ollama, while keeping the app usable without paid APIs.
- Improve classification and priority rules with additional tests and examples.
- Add authentication and agent assignment if the project is extended for multi-user use.
- Add continuous integration to run tests on each push.
- Add pagination or server-side sorting if the ticket dataset grows significantly.

## What I Learned

This project gave me practical experience with Python application structure, Flask routes and templates, SQLite persistence, input validation, error handling, automated testing, debugging, responsive UI development, and Git-based version control.

## Author

**Naveen Menon**

- GitHub: https://github.com/naveenmenon7
- Portfolio: https://naveenmenon7.github.io/
