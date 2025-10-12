from notion_client import Client
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()

notion = Client(auth=os.getenv("NOTION_KEY"))

database_id : str = os.getenv("DATABASE_ID") 
response = notion.databases.query(database_id=database_id) 

pages = response["results"]

pprint(pages)
for page in pages:
    props = page["properties"]

    nom_contact = props["Nom de famille du contact (1)"]["rich_text"][0]["plain_text"] if props["Nom de famille du contact (1)"]["rich_text"] else ""
    email = props["E-mail"]["email"] if props["E-mail"]["email"] else ""
    statut = props["Étape"]["status"]["name"] if props["Étape"]["status"] else ""
    entreprise = props["Nom entreprise"]["rich_text"][0]["plain_text"] if props["Nom entreprise"]["rich_text"] else ""

    print(f"{nom_contact} - {email} - {statut} - {entreprise}")
