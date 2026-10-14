# AI Support Ticket Assistant

A Python-based support ticket classification system that categorizes customer messages, assigns priority levels, and validates user input. The project demonstrates fundamental software development concepts through a practical customer support use case.

## Features

- **Ticket Classification:** Categorizes messages into Billing, Account Access, Technical Support, or General Inquiry.
- **Priority Detection:** Assigns High, Medium, or Low priority based on predefined keywords and phrases.
- **Input Validation:** Rejects empty messages, whitespace-only messages, and non-string inputs.
- **Error Handling:** Handles invalid inputs using Python exceptions.
- **Automated Testing:** Includes a test suite covering classification rules, priority detection, and edge cases.

## Technologies Used

- Python
- `unittest` for automated testing
- Git and GitHub for version control

## Project Structure

```text
AI-Support-Ticket-Assistant/
├── main.py
├── tests/
│   └── test_main.py
├── Docs/
│   └── Learning_Log.md
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- Python 3 installed
- Git, if you want to clone the repository

### Installation

Clone the repository:

```bash
git clone https://github.com/naveenmenon7/AI-Support-Ticket-Assistant.git
```

Navigate to the project directory:

```bash
cd AI-Support-Ticket-Assistant
```

### Run the application

```bash
python main.py
```

Enter a customer support message when prompted. The application displays the message, its category, and its assigned priority.

### Example Output

```text
Enter a customer support message: I've been charged twice for my subscription.

--- Ticket Details ---
Message: I've been charged twice for my subscription.
Category: Billing
Priority: High
```

### Run the automated tests

```bash
python -m unittest discover -s tests -v
```

The test suite covers ticket categories, priority rules, input validation, and selected edge cases.

## Current Limitations

- Classification relies on predefined keywords and phrases rather than a trained machine learning model or language model.
- Messages containing multiple issues are handled according to the order of the classification rules.
- Priority detection uses basic phrase matching and does not fully understand sentence context.

## Future Improvements

- Improve classification accuracy and context handling.
- Explore AI-powered classification.
- Add a user interface for submitting and reviewing tickets.
- Store ticket details and classification results.
- Expand automated testing.

## What I Learned

This project has helped me practise Python functions, conditional logic, input validation, exception handling, automated testing, debugging, refactoring, and version control.

## Author

**Naveen Menon**

- [GitHub](https://github.com/naveenmenon7)
- [Portfolio](https://naveenmenon7.github.io/)