from notion_mailer.service.notion_service import NotionService
from notion_mailer import logger
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()


class NotionSummarizer:
    """
    class to summarize notion pages using OpenAI GPT-4o-mini model
    """

    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables.")

        self.llm = ChatOpenAI(model="gpt-4o-mini", api_key=api_key)

        self.prompt = ChatPromptTemplate.from_template(
            "Voici la liste des candidatures :\n\n{candidatures}\n\n"
            "Fais un résumé clair et professionnel des candidatures, "
            "en indiquant les étapes, les entreprises, les lieux et tout point notable."
        )

        self.chain = self.prompt | self.llm | StrOutputParser()

    def summarize_all(self, pages: list) -> str:
        """
        Create a summary of all applications.
        """
        resume = []
        if not pages:
            return "Nothing to summarize."

        texte = "\n".join([
            f"- {getattr(p, 'etape', 'Étape inconnue')} | "
            f"{', '.join(getattr(p, 'secteur', []) or ['Secteur inconnu'])} | "
            f"{getattr(p, 'email', 'Aucun email')} | "
            f"{', '.join(getattr(p, 'civilite', []) or ['Civilité inconnue'])} | "
            f"{getattr(p, 'date_candidature', 'Pas de date')}"
            for p in pages
        ])

        try:
            resume = self.chain.invoke({"candidatures": texte})
        except Exception as e:
            logger.error(f"Error when resuming : {e}")

        return resume