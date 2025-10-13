from pprint import pprint
from src.notion_client import NotionClient
from src.Mailing.gmail_client import GmailClient
def main():
    notion = NotionClient()

    """
    prospects = notion.get_page_canditated()
    id_page = prospects[0]["id"]
    notion.update_page_status(id_page, 'A prospecter')
    pprint(len(notion.get_page_prospect()))
    """
    mail_body = "Bonjour \n Veuillez reçevoir cette candidature \n Cordialement,\n Meline Biguet"
    mail = GmailClient()
    mail.send_mail("hyaolire@gmail.com", "Candidature spontanée", mail_body)

if __name__ == "__main__":
    main()