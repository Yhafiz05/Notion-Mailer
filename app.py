import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox
from PyQt6.QtCore import Qt
from notion_mailer.service.notion_service import NotionService
from notion_mailer.service.notion_mail_service import NotionMailService
from notion_mailer.mailing.smtp_client import SmtpClient
from notion_mailer import logger


class NotionMailerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Notion Mailer")
        self.setGeometry(200, 200, 350, 200)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        title = QLabel("Notion Mailer Interface")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #3A6EA5;")

        send_mail_btn = QPushButton("📤 Envoyer les mails de candidature")
        send_mail_btn.clicked.connect(self.send_mail)
        send_mail_btn.setStyleSheet("font-size: 14px; padding: 10px;")

        send_relance_btn = QPushButton("🔁 Envoyer les mails de relance")
        send_relance_btn.clicked.connect(self.send_relance)
        send_relance_btn.setStyleSheet("font-size: 14px; padding: 10px;")

        layout.addWidget(title)
        layout.addWidget(send_mail_btn)
        layout.addWidget(send_relance_btn)
        self.setLayout(layout)

    def send_mail(self):
        try:
            client = NotionService()
            pages = client.get_page_prospect()
            if len(pages) == 0:
                QMessageBox.information(self, "Information", "Aucun mail de candidature à envoyer.")
                return

            for page in pages:
                mail = NotionMailService()
                mail_template = mail.get_mails_candidature_by_type(page.secteur)
                mail_template.render_mail(page)
                smtp = SmtpClient()
                smtp.send_mail(
                    recipient=page.email,
                    subject=mail_template.subject,
                    content=mail_template.body,
                    attachement=mail_template.attachments
                )
                client.update_page_status(page.id, "Candidaté")
                client.update_date_candidature(page.id)

            QMessageBox.information(self, "Succès ✅", f"{len(pages)} mails envoyés avec succès !")

        except Exception as e:
            logger.error(f"Erreur envoi candidature: {e}")
            QMessageBox.critical(self, "Erreur ❌", str(e))

    def send_relance(self):
        try:
            client = NotionService()
            pages = client.get_page_canditated_expired()
            if len(pages) == 0:
                QMessageBox.information(self, "Information", "Aucun mail de relance à envoyer.")
                return

            for page in pages:
                mail = NotionMailService()
                mail_template = mail.get_mails_relance_by_type(page.secteur)
                mail_template.render_mail(page)
                smtp = SmtpClient()
                smtp.send_mail(
                    recipient=page.email,
                    subject=mail_template.subject,
                    content=mail_template.body,
                    attachement=mail_template.attachments
                )
                client.update_page_status(page.id, "Première relance")
                client.update_date_relance(page.id)

            QMessageBox.information(self, "Succès ✅", f"{len(pages)} relances envoyées avec succès !")

        except Exception as e:
            logger.error(f"Erreur envoi relance: {e}")
            QMessageBox.critical(self, "Erreur ❌", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotionMailerApp()
    window.show()
    sys.exit(app.exec())
