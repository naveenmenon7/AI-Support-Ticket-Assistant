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


## Session 3: Ticket Priority Detection

### Objective
Extend the ticket classifier to assign a priority to each support message.

### Features implemented
- High priority detection
- Medium priority detection
- Low priority as the default
- Separate function for priority determination

### Concepts learned
- Python lists
- For loops
- Keyword matching
- Returning values from functions
- Using multiple functions to process the same input

### Testing
- Duplicate payment message: High
- Password-related message: Medium
- General inquiry: Low

### Status
Completed. All three manual test cases passed.

### Limitations
Priority detection relies on predefined keywords and may not
correctly interpret every message or determine its real-world urgency.

### Next steps
Introduce automated tests and improve input handling.

----------------------------------------------------------------------------------------------


## Session 4: Automated Testing

### Objective
Create automated tests for ticket classification and priority detection.

### Concepts learned
- Python's unittest framework
- Test cases and assertions
- Importing functions from another module
- The __name__ == "__main__" guard
- Test discovery and command-line options

### Tests implemented
- Billing ticket classification and priority
- Account access classification and priority
- Technical support classification and priority
- General inquiry classification and priority

### Verification
All four automated tests passed.

### Status
Completed.

### Next steps
Improve classification rules and add edge-case tests.

-------------------------------------------------------------------------------------------------

