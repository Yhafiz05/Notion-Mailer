from notion_client import Client
from dotenv import load_dotenv

class TemplateCandidature:
    def __init__(self):
        self.client = Client(auth=os.getenv("NOTION_KEY"))