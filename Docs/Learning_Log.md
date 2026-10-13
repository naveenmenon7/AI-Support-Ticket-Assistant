# Learning Log — AI Support Ticket Assistant

## Session 1: Environment Setup

### Objective
Set up Python and VS Code and run the first program.

### Concepts learned
- Running a Python script
- Variables
- Strings
- The print() function
- Saving and executing a file

### Status
Completed.

### Notes
Record any installation issues, commands used, and what was learned.

-----------------------------------------------------------------------------------

## Session 2: Rule-Based Ticket Classification

### Objective
Build a Python function that categorizes customer support messages.

### Features implemented
- Billing classification
- Account Access classification
- Technical Support classification
- General Inquiry fallback category
- Interactive input through the terminal

### Concepts learned
- Python functions and return values
- if, elif, and else statements
- String methods and lowercase conversion
- Basic keyword-based classification

### Testing
- Duplicate payment message: Billing
- Password and login message: Account Access
- Application crash message: Technical Support

### Status
Completed. All three test cases passed.

### Limitations
The classifier relies on predefined keywords and may misclassify
messages that use unfamiliar wording or contain multiple issues.

### Next steps
Improve classification, add ticket priorities, and introduce
automated tests.

-------------------------------------------------------------------------------------------
