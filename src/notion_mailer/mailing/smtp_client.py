import os
from dotenv import load_dotenv
import smtplib, ssl
from email.message import EmailMessage
from notion_mailer import logger
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SmtpClient():
    
    def __init__(self) -> None:
        load_dotenv()
        self.sender = os.getenv("MAIL_USER")
        self.password = os.getenv("MAIL_PASS")
        self.port = 465
        self.smtp_server = "smtp.gmail.com"
        self.server = None
        

    def send_mail(self, recipient: str, subject: str, content: str) -> None:
        """Send a mail to a recipient

        Args:
            recipient (str): Address of the recipient
            subject (str): Subject of the mail
            content (str): Body of the mail
        """
        ssl_context = ssl.create_default_context()
        msg = MIMEMultipart("alternative")
        msg["FROM"] = self.sender
        msg["TO"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(content, "plain", "UTF-8"))
        try :
            with smtplib.SMTP_SSL(self.smtp_server, self.port, context=ssl_context) as service :
                service.login(self.sender, self.password)
            
                message = f"Subject: {subject}\n\n{content}"

                service.send_message(msg)
            
                logger.info(f"Mail send to {recipient}")
            
        except smtplib.SMTPAuthenticationError as e:
            logger.error("Please check your app password")
        except Exception as e:
            logger.error(f"{e}")
