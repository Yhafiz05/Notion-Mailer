from notion_mailer.mapper.mapper_page import map_to_page_dto
import json

def test_map_to_dto():
    test = '''[
        {
            "object": "page",
            "id": "28a04b2b-e654-804f-bf64-cde035c95b96",
            "created_time": "2025-10-12T22:28:00.000Z",
            "last_edited_time": "2025-10-13T18:48:00.000Z",
            "created_by": {
                "object": "user",
                "id": "d5bb7f00-fec4-496c-8b2e-21ecedfd3ba3"
            },
            "last_edited_by": {
                "object": "user",
                "id": "ad21d76e-b649-426f-8b2e-f9ef52b509dc"
            },
            "cover": null,
            "icon": null,
            "parent": {
                "type": "database_id",
                "database_id": "28a04b2b-e654-81f8-a38b-f9ba6515624e"
            },
            "archived": false,
            "in_trash": false,
            "is_locked": false,
            "properties": {
                "Candidaté le": {
                    "id": "%3B%7DQd",
                    "type": "date",
                    "date": null
                },
                "Statut mail": {
                    "id": "%3ETSA",
                    "type": "multi_select",
                    "multi_select": []
                },
                "Nom de famille": {
                    "id": "%3EUhz",
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Yaolire2",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "Yaolire2",
                            "href": null
                        }
                    ]
                },
                "Lien pour candidature": {
                    "id": "%3ExpI",
                    "type": "url",
                    "url": null
                },
                "Secteur": {
                    "id": "%40_%40v",
                    "type": "multi_select",
                    "multi_select": [
                        {
                            "id": ">?fV",
                            "name": "Dermocosmétique",
                            "color": "blue"
                        }
                    ]
                },
                "Lieu": {
                    "id": "D3u%3C",
                    "type": "select",
                    "select": {
                        "id": "87f38ecd-27bb-4a33-9f00-2f103325e1cc",
                        "name": "Toulouse",
                        "color": "pink"
                    }
                },
                "Clic le ": {
                    "id": "EZT-",
                    "type": "date",
                    "date": null
                },
                "Notes de l'étape": {
                    "id": "MCw%40",
                    "type": "rich_text",
                    "rich_text": []
                },
                "Étape": {
                    "id": "MYcP",
                    "type": "status",
                    "status": {
                        "id": "tkm<",
                        "name": "A prospecter",
                        "color": "orange"
                    }
                },
                "Contact": {
                    "id": "S%2FSh",
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Directeur",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "Directeur",
                            "href": null
                        }
                    ]
                },
                "Nom entreprise": {
                    "id": "STDh",
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Pierre Fabre",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "Pierre Fabre",
                            "href": null
                        }
                    ]
                },
                "Type de candidature": {
                    "id": "X%3CPr",
                    "type": "multi_select",
                    "multi_select": [
                        {
                            "id": "pE[<",
                            "name": "Spontanée",
                            "color": "yellow"
                        }
                    ]
                },
                "Téléphone": {
                    "id": "a_%3AQ",
                    "type": "phone_number",
                    "phone_number": null
                },
                "Dossier de motivation": {
                    "id": "b%3CxB",
                    "type": "files",
                    "files": []
                },
                "Mail": {
                    "id": "jvVl",
                    "type": "rich_text",
                    "rich_text": []
                },
                "E-mail": {
                    "id": "n%3AN.",
                    "type": "email",
                    "email": "hyaolire@gmail.com"
                },
                "Civilité": {
                    "id": "q%3CAP",
                    "type": "multi_select",
                    "multi_select": [
                        {
                            "id": "prG;",
                            "name": "Monsieur",
                            "color": "blue"
                        }
                    ]
                },
                "Relancé le (J+7)": {
                    "id": "qa%7CI",
                    "type": "date",
                    "date": null
                },
                "Remercié et synthèse le": {
                    "id": "rCih",
                    "type": "date",
                    "date": null
                },
                "Nom": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Chef de produit - Pierre Fabre 2",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "Chef de produit - Pierre Fabre 2",
                            "href": null
                        }
                    ]
                },
                "Site Web": {
                    "id": "prop_1",
                    "type": "url",
                    "url": null
                }
            },
            "url": "https://www.notion.so/Chef-de-produit-Pierre-Fabre-2-28a04b2be654804fbf64cde035c95b96",
            "public_url": null
        }
    ]'''
    test_py = json.loads(test)
    result = map_to_page_dto(test_py)
    assert len(result) == 1
    assert result[0].email == "hyaolire@gmail.com"
    assert result[0].date_candidature == None
    