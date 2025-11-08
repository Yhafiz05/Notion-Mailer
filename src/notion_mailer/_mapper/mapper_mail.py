from notion_mailer._dto.mailDTO import MailDTO

def map_to_mail_dto(responses: list[dict]) -> list[MailDTO]:
    """
    Maps a Notion API response to a MailDTO object.

    Args:
        response (list(dict)): The Notion API response.

    Returns:
        list[MailDTO]: A list of mapped MailDTO object.
    """
    dtos = []
    for response in responses:
        
        properties = response.get("properties", {})
        
        subject = properties.get("Objet mail candidature", {}).get("rich_text", [{}])[0].get("plain_text", "")
        body = "".join([t.get("plain_text", "") for t in properties.get("Corps mail candidature", {}).get("rich_text", [])])
        attachements = properties.get("Dossier de motivation", {}).get("files", [{}])[0].get("file", {}).get("url", "")

        dtos.append(
            MailDTO(
                subject=subject,
                body=body,
                attachments=attachements
            )
        )

    return dtos