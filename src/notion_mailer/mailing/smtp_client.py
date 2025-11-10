import os
from dotenv import load_dotenv
import smtplib, ssl
from notion_mailer import logger
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
from email.mime.base import MIMEBase
from email import encoders
from notion_mailer.mailing.signature import signature_html

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
        <body style="font-size:11pt; font-family:Arial, sans-serif;">
        <p>{html_content}</p>
        {signature_html}
        </body>
        </html>
        """
        msg.attach(MIMEText(content, "plain", "UTF-8"))
        msg.attach(MIMEText(html_version, "html", "utf-8"))
        #dir = os.path.dirname(os.path.abspath(__file__))
        #image_path = os.path.join(dir,"data/image004.png")
        #logo_path = os.path.join(dir,"data/linkedln.png")
        """
        with open(image_path, "rb") as img:
            signature_img = MIMEImage(img.read())
            signature_img.add_header("Content-ID", "<signature_image>")
            msg.attach(signature_img)

        with open(logo_path, "rb") as img:
            linkedin_icon = MIMEImage(img.read())
            linkedin_icon.add_header("Content-ID", "<linkedin_icon>")
            msg.attach(linkedin_icon)
        """    
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
