from notion_mailer.mailing.smtp_client import SmtpClient


class GmailClient(SmtpClient):
    def __init__(self):
        super().__init__()
        self._smtp_server = "smtp.gmail.com"
        