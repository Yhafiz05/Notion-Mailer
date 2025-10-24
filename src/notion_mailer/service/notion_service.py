from notion_client import Client
from notion_mailer._mapper.mapper_page import map_to_page_dto
import os
from dotenv import load_dotenv

class NotionService :
    
    def __init__(self):
        load_dotenv()
        self.client = Client(auth=os.getenv("NOTION_KEY"))
        self.database_id : str = os.getenv("DATABASE_ID")
        
    def get_pages(self) -> list :
        """Retrieve all pages in the database

        Returns:
            list: List of all pages
        """
        response = self.client.databases.query(database_id=self.database_id) 
        response_dto = map_to_page_dto(response["results"])
        return response_dto
    
    def get_page_prospect(self) -> list:
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
        
    def get_page_canditated(self) -> list :
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
    