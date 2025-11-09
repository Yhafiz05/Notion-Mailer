from notion_mailer import logger
from notion_mailer.service.notion_service import NotionService
from notion_mailer.service.notion_mail_service import NotionMailService
from notion_mailer.mailing.smtp_client import SmtpClient

def send_mail():
    client: NotionService = NotionService()
    pages = client.get_page_prospect()
    for page in pages:
        try:
            mail : NotionMailService = NotionMailService()
            mail_template = mail.get_mails_candidature_by_type(page.secteur)
            mail_template.render_mail(page)
            smtp : SmtpClient = SmtpClient()
            smtp.send_mail(
                recipient=page.email,
                subject=mail_template.subject,
                content=mail_template.body,
                attachement=mail_template.attachments
            )
        except Exception as e:
            logger.error(f"Failed to send mail to {page.email}: {e}")
        client.update_page_status(page.id, "Candidature envoyée")
        
def main():
    client: NotionService = NotionService()
    pages = client.get_page_prospect()
    page = pages[0]
    print(page)
    
    mail: NotionMailService = NotionMailService()
    mail_template = mail.get_mails_candidature_by_type(page.secteur)
    mail_template.render_mail(page)
    print(mail_template.body)

    smtp: SmtpClient = SmtpClient()
    smtp.send_mail(
        recipient=page.email,
        subject=mail_template.subject,
        content=mail_template.body,
        attachement=mail_template.attachments
    )
    
if __name__ == "__main__":
    main()