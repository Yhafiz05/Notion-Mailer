# Notion-Mailer

A simple way to automate sending emails and application reminders

## Create a .env file at the root of the project

Add some environnement variables to connect to your notion intégration & database

```
NOTION_KEY=$Your_token
DATABASE_ID=$Your_id$
MAIL_ID=$Your_mail_id$
```

Begin by installing runtime and developpement dependencies

```bash
pip install -r requirements.txt
pip install -e .[dev]
```
