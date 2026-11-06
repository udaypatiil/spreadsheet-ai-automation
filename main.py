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
