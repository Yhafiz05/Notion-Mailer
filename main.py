from notion_mailer import logger
from notion_mailer.service.notion_service import NotionService
from notion_mailer.service.notion_mail_service import NotionMailService
from notion_mailer.mailing.smtp_client import SmtpClient

def send_mail():
    client: NotionService = NotionService()
    pages = client.get_page_prospect()
    if len(pages) == 0:
        logger.info("No mails to send today...")
        return
    logger.info(f"Sending mails to {len(pages)} prospects...")
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
            client.update_page_status(page.id, "Candidaté")
            client.update_date_candidature(page.id)
        except Exception as e:
            logger.error(f"Failed to send mail to {page.email}: {e}")

def send_relance_mail():
    client: NotionService = NotionService()
    pages  = client.get_page_canditated_expired()
    if len(pages) == 0:
        logger.info("No relance mails to send today...")
        return
    logger.info(f"Sending relance mails to {len(pages)} candidated...")
    for page in pages:
        try:
            mail: NotionMailService = NotionMailService()
            mail_template = mail.get_mails_relance_by_type(page.secteur)
            mail_template.render_mail(page)
            smtp: SmtpClient = SmtpClient()
            smtp.send_mail(
                recipient=page.email,
                subject=mail_template.subject,
                content=mail_template.body,
                attachement=mail_template.attachments
            )
            client.update_page_status(page.id, "Première relance")
            client.update_date_relance(page.id)
        except Exception as e:
            logger.error(f"Failed to send relance mail to {page.email}: {e}")
            
def main():
    client: NotionService = NotionService()
    pages = client.get_page_canditated_expired()
    page = pages[0]
    print(page)
    """
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
    """
    
if __name__ == "__main__":
    send_relance_mail()