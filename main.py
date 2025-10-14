from pprint import pprint
from notion_mailer.service.notion_service import NotionService
from notion_mailer.mailing.smtp_client import SmtpClient
def main():
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
    pprint(notion.get_pages())

if __name__ == "__main__":
    main()