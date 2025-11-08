import os
from dotenv import load_dotenv
import smtplib, ssl
from notion_mailer import logger
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
from email.mime.base import MIMEBase
from email import encoders

class SmtpClient():
    
    def __init__(self) -> None:
        load_dotenv()
        self.sender = os.getenv("MAIL_USER")
        self.password = os.getenv("MAIL_PASS")
        self.port = 465
        self.smtp_server = "smtp.gmail.com"
        self.server = None
        

    def send_mail(self, recipient: str, subject: str, content: str, attachement=None) -> None:
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
        html_content = content.replace("\n", "<br>")
        
        html_version = f"""
        <html>
        <body>
        <p>{html_content}</p>
        </body>
        </html>
        """
        msg.attach(MIMEText(content, "plain", "UTF-8"))
        msg.attach(MIMEText(html_version, "html", "utf-8"))
                
        if attachement:
            response = requests.get(attachement)
            file_content = response.content
            file_name = "Dossier_de_motivation.pdf"

            part = MIMEBase("application", "pdf")
            part.set_payload(file_content)
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f'attachment; filename="{file_name}"',
            )

            msg.attach(part)
        try :
            with smtplib.SMTP_SSL(self.smtp_server, self.port, context=ssl_context) as service :
                service.login(self.sender, self.password)
            
                service.send_message(msg)
            
                logger.info(f"Mail send to {recipient}")
            
        except smtplib.SMTPAuthenticationError as e:
            logger.error("Please check your app password")
        except Exception as e:
            logger.error(f"{e}")
