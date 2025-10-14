from notion_mailer.service.notion_service import NotionService


def test_get_pages_returns_list():
    notionService = NotionService()
    pages = notionService.get_pages()
    assert isinstance(pages, list)

def test_get_page_prospect_returns_list():
    notion_service = NotionService()
    prospects = notion_service.get_page_prospect()
    
    assert isinstance(prospects, list)
    for page in prospects:
        assert page['properties']['Étape']['status']['name'] == "A prospecter"
