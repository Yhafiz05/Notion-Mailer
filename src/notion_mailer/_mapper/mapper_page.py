from notion_mailer._dto.pageDTO import PageDTO

def map_to_page_dto(responses: list[dict]) -> list[PageDTO]:
    """
    Maps a Notion API response to a PageDTO object.

    Args:
        response (list(dict)): The Notion API response.

    Returns:
        list[PageDTO]: A list of mapped PageDTO object.
    """
    dtos = []
    for response in responses:
        
        properties = response.get("properties", {})

        id = response.get("id", "")
        etape = properties.get("Étape", {}).get("status", {}).get("name", "")
        secteur = ", ".join([item.get("name", "") for item in properties.get("Secteur", {}).get("multi_select", [])])
        email = properties.get("E-mail", {}).get("email", "")
        civilite = ", ".join([item.get("name", "") for item in properties.get("Civilité", {}).get("multi_select", [])])
        date_candidature = properties.get("Candidaté le", {}).get("date", "")
        entreprise = properties.get("Nom entreprise", {}).get("rich_text", [{}])[0].get("plain_text", "")
        nom_famille = properties.get("Nom de famille", {}).get("rich_text", [{}])[0].get("plain_text", "")

        dtos.append(
            PageDTO(
                id=id,
                etape=etape,
                secteur=secteur,
                nom_entreprise=entreprise,
                email=email,
                civilite=civilite,
                nom_famille=nom_famille,
                date_canditature=date_candidature
            )
        )

    return dtos