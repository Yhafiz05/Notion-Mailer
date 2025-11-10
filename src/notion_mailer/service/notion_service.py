from notion_client import Client
from notion_mailer._mapper.mapper_page import map_to_page_dto
from notion_mailer._dto.pageDTO import PageDTO
import os
from datetime import date, timedelta
from dotenv import load_dotenv

class NotionService :
    
    def __init__(self):
        load_dotenv()
        self.client = Client(auth=os.getenv("NOTION_KEY"))
        self.database_id : str = os.getenv("DATABASE_ID")
        
    def get_pages(self) -> list[PageDTO] :
        """Retrieve all pages in the database

        Returns:
            list: List of all pages
        """
        response = self.client.databases.query(database_id=self.database_id) 
        response_dto = map_to_page_dto(response["results"])
        return response_dto
    
    def get_page_prospect(self) -> list[PageDTO]:
        """Retrieve pages with A Prospecter status

        Returns:
            list: List of all pages
        """
        response = self.client.databases.query(
            database_id=self.database_id,
            filter={
                "property": "Étape",
                "status": {
                    "equals": "A prospecter"
                }
            }
        )
        response_dto = map_to_page_dto(response["results"])
        return response_dto
    
    def update_page_status(self, page_id: str, status: str) -> None :
        """Update the status of a page

        Args:
            page_id (str): Id of the specific page
            status (str): The status you want to modify
        """
        self.client.pages.update(
            page_id=page_id,
            properties={
                "Étape": {
                    "status": {
                        "name": status
                    }
                }
            }
        )
        
    def get_page_canditated(self) -> list[PageDTO] :
        """Retrieve pages with Candidaté status

        Returns:
            list: List of all pages
        """
        response = self.client.databases.query(
            database_id=self.database_id,
            filter={
                "property": "Étape",
                "status": {
                    "equals": "Candidaté"
                }
            }
        )
        response_dto = map_to_page_dto(response["results"])
        return response_dto
    
    def update_date_candidature(self, page_id: str) -> None:
        """Update the date of candidature to the current date

        Args:
            page_id (str): Id of the specific page
        """
        today = date.today().isoformat()
        self.client.pages.update(
            page_id=page_id,
            properties={
                "Candidaté le": {
                    "date": {
                        "start": today
                    }
                }
            }
        )

    def get_page_canditated_expired(self) -> list[PageDTO]:
        """Retrieve pages with Candidaté status where 'Candidaté le' is older than 7 days."""
        today = date.today()
        seven_days_ago = (today - timedelta(days=7)).isoformat()

        response = self.client.databases.query(
            database_id=self.database_id,
            filter={
                "and": [
                    {
                        "property": "Étape",
                        "status": {
                            "equals": "Candidaté"
                        }
                    },
                    {
                        "property": "Candidaté le",
                        "date": {
                            "on_or_before": seven_days_ago
                        }
                    }
                ]
            }
        )

        response_dto = map_to_page_dto(response["results"])
        return response_dto
    
    def update_date_relance(self, page_id: str) -> None:
        """Update the date of candidature to the current date

        Args:
            page_id (str): Id of the specific page
        """
        today = date.today().isoformat()
        self.client.pages.update(
            page_id=page_id,
            properties={
                "Relancé le (J+7)": {
                    "date": {
                        "start": today
                    }
                }
            }
        )