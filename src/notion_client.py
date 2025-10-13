from notion_client import Client
import os
from dotenv import load_dotenv


class NotionClient :
    
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
        return response["results"]
    
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
        return response["results"]
    
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
        return response["results"]
    