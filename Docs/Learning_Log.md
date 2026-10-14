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

**## Session 5: Input Validation and Error Handling**

**### Objective**
Validate customer support messages and handle invalid inputs safely.

**### Features implemented**
\- Message validation using a separate `validate_message()` function
\- Rejection of empty messages
\- Rejection of whitespace-only messages
\- Type checking to ensure the input is a string
\- Error handling using `ValueError` and `TypeError`
\- User-friendly error messages using `try` and `except`

**### Concepts learned**
\- Input validation
\- Python's exception handling
\- Raising exceptions using `raise`
\- Difference between `ValueError` and `TypeError`
\- Handling invalid inputs without crashing the program
\- Writing automated tests for invalid inputs

**### Testing**
\- Empty message: Rejected
\- Whitespace-only message: Rejected
\- Non-string input: Rejected
\- Valid customer messages: Processed correctly

**### Status**
Completed. All input validation tests passed.

**### Limitations**
The validation checks basic input requirements but does not verify whether a message contains meaningful customer support information.

**### Next steps**
Improve priority detection, handle edge cases, and expand automated test coverage.

\----------------------------------------------------------------------------------------------


**## Session 6: Improving Ticket Priority Classification**

**### Objective**
Improve priority detection by handling different message variations and testing edge cases.

**### Features implemented**
\- Expanded high-priority phrase detection
\- Added security-related phrases such as "account was hacked" and "account was compromised"
\- Introduced basic handling for negated phrases
\- Expanded automated tests for priority classification
\- Fixed a classification bug caused by an unrecognized phrase variation

**### Concepts learned**
\- Limitations of exact phrase matching
\- Importance of checking high-priority rules before medium-priority rules
\- Testing edge cases
\- Debugging failed unit tests
\- Using expected and actual values to identify bugs
\- Verifying code changes by rerunning the complete test suite

**### Testing**
\- Billing ticket classification and priority
\- Account access ticket classification and priority
\- Technical support ticket classification and priority
\- General inquiry classification and priority
\- Negated duplicate-charge message: Not High
\- Hacked account message: High
\- Ordinary payment question: Medium
\- Invalid input handling

**### Verification**
All 10 automated tests passed using `python -m unittest discover -s tests -v`.

**### Status**
Completed. All 10 automated tests passed.

**### Limitations**
The classifier still relies on predefined phrases and simple keyword matching. Negation handling is basic and may not correctly interpret more complex sentences or every variation of customer messages.

**### Next steps**
Refactor the classification rules for better maintainability, improve handling of varied customer messages, and continue developing the project toward an AI-assisted support ticket system.

\----------------------------------------------------------------------------------------------

**## Session 7: Code Refactoring and Maintainability**

**### Objective**
Refactor the ticket classification and priority detection functions to improve readability and maintainability without changing their expected behaviour.

**### Improvements implemented**
\- Grouped ticket classification keywords into separate lists for each category
\- Used Python's `any()` function to simplify keyword matching
\- Simplified medium-priority detection
\- Reduced unnecessary conditional logic
\- Preserved the existing category and priority rules

**### Concepts learned**
\- Code refactoring
\- Writing readable and maintainable functions
\- Using lists to organize related data
\- Using the `any()` function to check multiple conditions
\- Maintaining rule precedence in a classification system
\- Verifying behaviour after code changes

**### Testing**
\- Ran all 10 automated unit tests
\- Tested a duplicate-payment message: Billing, High
\- Tested a password and login message: Account Access, Medium
\- Tested a general inquiry: General Inquiry, Low

**### Status**
Completed. All 10 automated tests passed, and the three manual test cases produced the expected results.

**### Limitations**
The classifier still relies on predefined keywords and phrases. The negation handling is basic and may not correctly interpret every sentence.

**### Next steps**
Improve classification accuracy, expand edge-case testing, and prepare the project for portfolio presentation.

\----------------------------------------------------------------------------------------------

**## Session 8: Edge-Case Testing**

**### Objective**
Expand automated test coverage to identify limitations in rule-based ticket classification and priority detection.

**### Tests implemented**
\- Password manager question
\- Message containing both billing and account-access issues
\- Application not working
\- Negated application crash
\- Existing billing, account access, technical support, and general inquiry tests
\- Input validation and priority edge cases

**### Concepts learned**
\- Edge-case testing
\- Test-driven development
\- Understanding expected versus actual behaviour
\- Testing messages containing multiple keywords
\- Recognizing limitations of exact phrase matching
\- Distinguishing passing tests from comprehensive coverage

**### Verification**
All 14 automated tests passed using `python -m unittest discover -s tests -v`.

**### Status**
Completed. The test suite covers additional message variations and documents several limitations of keyword-based classification.

**### Limitations**
The classifier still relies on predefined keywords and phrases. Passing individual tests does not guarantee that every variation of a customer message will be classified correctly.

**### Next steps**
Improve the priority detection logic, add more meaningful context-handling tests, and prepare the application for portfolio presentation.

\----------------------------------------------------------------------------------------------

**## Session 9: Improving Priority Detection**

**### Objective**
Improve high-priority ticket detection by recognizing additional variations of customer messages.

**### Improvements implemented**
\- Added "unable to access" to the high-priority phrase list
\- Improved detection of account-access issues
\- Added an automated test for the new phrase
\- Preserved the existing priority classification rules

**### Concepts learned**
\- Improving rule-based classification
\- Recognizing different ways users describe the same issue
\- Regression testing
\- Keeping automated tests aligned with code changes
\- Making small, targeted improvements without rewriting the entire system

**### Testing**
\- Verified existing billing, account access, technical support, and general inquiry cases
\- Tested "I cannot access my account"
\- Tested "I am unable to access my account"
\- Verified that ordinary account questions remain Medium priority

**### Verification**
All 17 automated tests passed using `python -m unittest discover -s tests -v`.

**### Status**
Completed. The classifier recognizes an additional account-access phrase, and automated coverage has been expanded.

**### Limitations**
The classifier still relies on predefined keywords and phrases. It does not fully understand context, sentiment, or the real-world urgency of a message.

**### Next steps**
Perform a final code review, improve the README, prepare realistic example outputs, and make the project ready to showcase on the portfolio website.

\----------------------------------------------------------------------------------------------

**## Session 10: Flask Web Application and SQLite Integration**

**### Objective**
Extend the command-line ticket classifier into a browser-based application with persistent ticket storage.

**### Features implemented**
\- Created a web interface using Flask
\- Added a form for submitting customer support messages
\- Connected Flask to the existing Python classification functions
\- Displayed ticket categories and priorities in the browser
\- Created an SQLite database to store ticket records
\- Implemented ticket history with message, category, priority, and timestamp
\- Applied the Post/Redirect/Get pattern to prevent duplicate submissions when refreshing the results page
\- Added automated tests for Flask routes and database operations

**### Concepts learned**
\- Flask routes and HTTP GET and POST requests
\- HTML forms and server-side template rendering
\- Integrating existing Python modules into a web application
\- SQLite tables, database connections, and SQL queries
\- Persistent data storage
\- The Post/Redirect/Get pattern
\- Flask's test client and temporary test databases
\- Automated testing of web application behaviour

**### Testing**
\- Verified that the homepage loads successfully
\- Tested ticket submission and database persistence
\- Verified that refreshing the page does not resubmit a ticket
\- Tested rejection of invalid messages
\- Confirmed that saved tickets appear in the history table
\- Reran the existing classification and input validation tests

**### Verification**
All 22 automated tests passed using `python -m unittest discover -s tests -v`.

**### Status**
Completed. The application now has a working browser interface, persistent ticket storage, ticket history, and automated tests covering both the classifier and web application.

**### Limitations**
Classification still relies on predefined keywords and phrases. The application currently runs locally and does not yet include AI-powered classification, authentication, or deployment.

**### Next steps**
Improve configuration and security, expand automated test coverage, integrate AI-powered classification, and prepare the application for portfolio presentation.

\----------------------------------------------------------------------------------------------

**## Session 11: Configuration and Project Security**

**### Objective**
Improve project configuration, protect local data, and make the application easier for other developers to set up.

**### Improvements implemented**
\- Updated `.gitignore` to exclude local SQLite databases
\- Added rules for environment-specific configuration and secrets
\- Created `requirements.txt` to document the Flask dependency
\- Updated the README with dependency installation instructions

**### Concepts learned**
\- Managing Python project dependencies
\- Using `requirements.txt` for reproducible setup
\- Protecting local databases and configuration files
\- Understanding the limitations of `.gitignore` for files already tracked by Git
\- Preparing a repository for other developers to clone and run

**### Testing**
\- Installed dependencies using `python -m pip install -r requirements.txt`
\- Ran the complete automated test suite
\- Verified that the application continued to work after configuration changes

**### Verification**
All 22 automated tests passed using `python -m unittest discover -s tests -v`.

**### Status**
Completed. The project now has documented dependencies and improved Git ignore rules for local data and configuration.

**### Next steps**
Integrate AI-powered ticket classification, expand automated testing, and prepare the application for portfolio presentation.

\----------------------------------------------------------------------------------------------