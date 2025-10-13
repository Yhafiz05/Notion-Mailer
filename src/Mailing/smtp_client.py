import os
from dotenv import load_dotenv
from abc import ABC
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SmtpClient(ABC):
    
    def __init__(self):
        load_dotenv()
        self.sender = os.getenv("MAIL_USER")
        self.password = os.getenv("MAIL_PASS")
        self.port = 587
        self.smtp_server = None
        
    def send_mail(self, recipient: str, subject: str, body:str):
        """Sending a mail 

        Args:
            recipient (_type_): Email of the recipient
            subject (_type_): Subject of the mail
            body (_type_): What you want to say
        """
        msg = MIMEMultipart()
        msg["From"] = self.sender
        msg["To"] = recipient
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        try:
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()
                server.login(self.sender, self.password)
                server.send_message(msg)
                print(f"Mail send to {recipient}")
        except Exception as e:
            print(f"An error occurs when sending the mail : {e}")