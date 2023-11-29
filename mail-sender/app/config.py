import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

HOST = os.environ.get("MAIL_HOST")
USERNAME = os.environ.get("MAIL_USERNAME")
PASSWORD = os.environ.get("MAIL_PASSWORD")
PORT = os.environ.get("MAIL_PORT", 465)

 # = {"from": None, "to": None, "subject": None, "body": None}
class MailBody(BaseModel):
    to: str | None = None
    subject: str | None = None
    body: str | None = None



