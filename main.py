import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from google.auth import api_key
from langchain.chat_models import init_chat_model
from googleapiclient.discovery import build
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')
SHEET_NAME = os.getenv('SHEET_NAME')

SENDER_EMAIL = os.getenv('SENDER_EMAIL')
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL')
SENDER_PASSWORD = os.getenv('SENDER_PASSWORD')
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

def get_spreadsheet_data():
    """Fetch spreadsheet data"""
    service = build('sheets', 'v4', developerKey=GOOGLE_API_KEY)
    all_rows = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=SHEET_NAME).execute()['values']
    with open('last_row.txt', 'r') as file:
        last_row = int(file.read())
    new_row = all_rows[last_row:]
    headers = all_rows[0]
    return all_rows, new_row,headers

def summarise_with_ai(text):
    system_prompt = """
    you are a helpful assistant that summarizes spreadsheet data.
    you will receive new rows that are were added to a Google spreadsheet.
    Please provide a clear, concise summary of this data. 
    """
    model = init_chat_model(
        model='gemini-3-flash-preview',
        model_provider='google_genai',
        api_key= os.getenv('GEMINI_API_KEY'))

    message = [{'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': f'here are the new rows from the spreadsheet.\n {text} '}]

    response = model.invoke(message).text
    return response



def send_email(subject, body):
    """Send email with the summary"""
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.send_message(msg)
    server.quit()
    print(f"Email send successfully to {RECIPIENT_EMAIL}")

all_rows, new_row, headers = get_spreadsheet_data()
total_rows = len(all_rows)
with open('last_row.txt', 'w') as file:
    file.write(str(total_rows))

message = f"Headers:{headers} \nNew row: {new_row}"
print(message)
summary = summarise_with_ai(message)

body = f"Here is a today's  summary \n\n{summary} \n\nThank You"
send_email(f"daily spreadsheet summary",body)


print("ALL_ROWS", all_rows)
print("NEW_ROW", new_row)
print(summary)