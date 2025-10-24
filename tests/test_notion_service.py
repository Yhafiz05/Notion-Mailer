from notion_mailer.service.notion_service import NotionService
from unittest.mock import patch, MagicMock

def test_get_pages_returns_list():
    fake_response = {
        "results": [
            {"id": "page1", "properties": {"Étape": {"status": {"name": "A prospecter"}}}},
            {"id": "page2", "properties": {"Étape": {"status": {"name": "Candidaté"}}}},
        ]
    }

    with patch("notion_mailer.service.notion_service.Client") as MockClient:
        mock_instance = MockClient.return_value
        mock_instance.databases.query.return_value = fake_response

        notion_service = NotionService()
        pages = notion_service.get_pages()

        mock_instance.databases.query.assert_called_once()
        assert isinstance(pages, list)

def test_get_page_prospect_returns_list():
    
    fake_response = {
        "results": [
            {"id": "page1", "properties": {"Étape": {"status": {"name": "A prospecter"}}}},
            {"id": "page2", "properties": {"Étape": {"status": {"name": "A prospecter"}}}},
        ]
    }
    
    with patch("notion_mailer.service.notion_service.Client") as MockClient:
        mock_instance = MockClient.return_value
        mock_instance.databases.query.return_value = fake_response
        
        notion_service = NotionService()
        prospects = notion_service.get_page_prospect()
        
        mock_instance.databases.query.assert_called_once_with(
            database_id=notion_service.database_id,
            filter={
                "property": "Étape",
                "status": {
                    "equals": "A prospecter"
                }
            }
        )
        assert isinstance(prospects, list)
        for page in prospects:
            assert page.etape == "A prospecter"
