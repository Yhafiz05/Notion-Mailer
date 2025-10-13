from src.Mailing.smtp_client import SmtpClient


class GmailClient(SmtpClient):
    def __init__(self):
        super().__init__()
        self._smtp_server = "smtp.gmail.com"
        
    def send_mail(self, recipient: str, subject: str, body: str) -> None:
        super().send_mail(recipient, subject, body)