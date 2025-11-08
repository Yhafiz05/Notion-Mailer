from notion_mailer.service.notion_service import NotionService
from notion_mailer.service.notion_mail_service import NotionMailService
from notion_mailer.mailing.smtp_client import SmtpClient
from dotenv import load_dotenv

def main():
    load_dotenv()
    notion = NotionService()

    """
    prospects = notion.get_page_canditated()
    id_page = prospects[0]["id"]
    notion.update_page_status(id_page, 'A prospecter')
    pprint(len(notion.get_page_prospect()))
    """
    #mail_body = "Bonjour \nVeuillez reçevoir cette candidature\nCordialement,\nMeline Biguet"
    #mail = SmtpClient()
    #mail.send_mail("hyaolire@gmail.com", "Candidature spontanée", mail_body)
    #pages = notion.get_pages()
    #summarizer = NotionSummarizer()
    #summary = summarizer.summarize_all(pages)
    #pprint(summary)
    """
    try:
        path = os.path.join(os.getcwd(), "template.pdf")
        download_file(os.getenv("TEMPLATE_FILE_ID"), path)
    except Exception as e:
        print(e)
    """
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