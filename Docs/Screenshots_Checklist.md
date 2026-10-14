# Screenshots Checklist

Capture clean screenshots from the running app at a desktop browser width. Use realistic sample tickets and avoid showing personal data, local file paths, terminal windows, or secret values.

Recommended screenshots:

1. `01-dashboard-light.png` — the Tickets page in light mode, with several sample tickets visible.
2. `02-dashboard-dark.png` — the same page in dark mode.
3. `03-new-ticket-dialog.png` — the New Ticket dialog, before submitting a message.
4. `04-ticket-analysis.png` — the resulting analysis view after submitting a representative support message.
5. `05-ticket-statuses.png` — a view showing Open, Pending, and Closed status indicators.
6. `06-spam-trash.png` — the Spam or Trash page, showing the active navigation state and Restore action.
7. `07-mobile-layout.png` — the responsive interface at a narrow viewport with the mobile sidebar open or closed.

## Suggested capture process

1. Start the application with `python app.py`.
2. Open the local Flask address in your browser.
3. Add a small set of dummy tickets such as a billing issue, login problem, and application error.
4. Pick one consistent accent colour and keep the browser zoom at 100%.
5. Capture the Tickets page in light mode and dark mode.
6. Capture the New Ticket dialog and one analysis result.
7. Capture Spam/Trash and a mobile-sized view.
8. Save images into a `screenshots/` folder in the project.

## Before committing screenshots

- Make sure every ticket message is fictional.
- Do not include API keys, `.env` contents, or sensitive personal information.
- Crop out browser tabs or desktop areas if they are distracting.
- If the screenshot folder is linked in `README.md`, confirm the relative image paths match the actual filenames.
