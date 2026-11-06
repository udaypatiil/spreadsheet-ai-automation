# Daily Spreadsheet AI Summary

An automation project that monitors new rows in a Google Spreadsheet, summarizes the new data using Google Gemini AI, and sends the summary through email.

## Features

- Fetches data from Google Sheets
- Detects newly added rows
- Uses Gemini AI to summarize new spreadsheet data
- Sends the AI-generated summary through Gmail SMTP
- Keeps track of the last processed row
- Uses environment variables for sensitive credentials

## How It Works

```text
Google Spreadsheet
       ↓
Fetch Spreadsheet Data
       ↓
Check Last Processed Row
       ↓
Find New Rows
       ↓
Gemini AI
       ↓
Generate Summary
       ↓
Send Email
```

## Technologies Used

- Python
- Google Sheets API
- Google Gemini
- LangChain
- SMTP
- Gmail
- python-dotenv

## Project Structure

```text
daily-spreadsheet-summary/
│
├── main.py
├── last_row.txt
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd daily-spreadsheet-summary
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
```

Activate it:

PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

Git Bash:

```bash
source .venv/Scripts/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key
GEMINI_API_KEY=your_gemini_api_key

SPREADSHEET_ID=your_spreadsheet_id
SHEET_NAME=Sheet1

SENDER_EMAIL=your_email@gmail.com
RECIPIENT_EMAIL=recipient_email@gmail.com
SENDER_PASSWORD=your_gmail_app_password
```

Never commit the `.env` file to GitHub.

### 5. Configure Google Sheets API

Create a Google Cloud project and enable the Google Sheets API.

Get the required API key and add it to the `.env` file.

### 6. Configure Gmail

Use a Gmail App Password for SMTP authentication instead of your normal Gmail password.

Add the App Password to:

```env
SENDER_PASSWORD=your_gmail_app_password
```

## Running the Project

Run:

```bash
python main.py
```

The program will:

1. Fetch spreadsheet data.
2. Read the previously processed row.
3. Detect new rows.
4. Send the new data to Gemini.
5. Generate a summary.
6. Send the summary through email.
7. Update `last_row.txt`.

## Example

Suppose the spreadsheet contains:

```text
Name    Product    Sales
Rahul   Laptop     50000
Amit    Phone      20000
```

If a new row is added:

```text
Priya   Tablet     30000
```

The application detects the new row and sends it to Gemini.

Gemini generates a summary such as:

```text
A new tablet sale worth ₹30,000 was recorded for Priya.
```

The summary is then sent by email.

## Security

Sensitive credentials are stored in environment variables.

The following files should never be committed:

```text
.env
.venv/
```

Make sure `.env` is included in `.gitignore`.

## Future Improvements

- Schedule the script to run automatically every day
- Add HTML email templates
- Add sales charts
- Track multiple spreadsheets
- Add error handling and logging
- Store processed rows in a database
- Add a dashboard
- Deploy the automation to a cloud service

## Author

Uday Patil