import os
from dotenv import load_dotenv
from notion_client import Client
from notion_mailer._mapper.mapper_mail import map_to_mail_dto
from notion_mailer._dto.mailDTO import MailDTO

class NotionMailService:
    def __init__(self):
        load_dotenv()
        self.client = Client(auth=os.getenv("NOTION_KEY"))
        self.mail_id: str = os.getenv("MAIL_ID")

    def get_mails(self) -> dict:
        """Retrieve mail template from Notion database

        Returns:
            dict: Mail template details
        """
        responses = self.client.databases.query(page_id=self.mail_id)
        mapped_mail = map_to_mail_dto(responses["results"])
        return mapped_mail
    
    def get_mails_relance_by_type(self, sector: str) -> MailDTO:
        """
        Retrieve mail template for relance by sector from Notion database
        Args:
            sector (str): name of the sector

        Returns:
            MailDTO: Mail template details
        """
        responses = self.client.databases.query(
            database_id=self.mail_id,
            filter={
                "and": [
                    {
                        "property": "Type de mail",
                        "multi_select": {
                            "contains": "Relance"
                        }
                    },
                    {
                        "property": "Secteur bis",
                        "multi_select": {
                            "contains": sector
                        }
                    }
                ]
            }
        )

        mapped_mail = map_to_mail_dto(responses["results"])
        return mapped_mail[0]
    
    def get_mails_candidature_by_type(self, sector: str) -> MailDTO:
        """
        Retrieve mail template for candidature by sector from Notion database
        Args:
            sector (str): name of the sector

        Returns:
            MailDTO: Mail template details
        """
        responses = self.client.databases.query(
            database_id=self.mail_id,
            filter={
                "and": [
                    {
                        "property": "Type de mail",
                        "multi_select": {
                            "contains": "Candidature"
                        }
                    },
                    {
                        "property": "Secteur bis",
                        "multi_select": {
                            "contains": sector
                        }
                    }
                ]
            }
        )

        mapped_mail = map_to_mail_dto(responses["results"])
        return mapped_mail[0]
    
