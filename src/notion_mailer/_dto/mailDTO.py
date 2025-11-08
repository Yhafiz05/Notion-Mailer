from notion_mailer._dto.pageDTO import PageDTO

class MailDTO:
    """
    MailDTO is a class thar represents the data transfer object for an email.
    """
    def __init__(self, subject: str, body: str, attachments: str):
        self._subject = subject
        self._body = body
        self._attachments = attachments
        
    @property
    def subject(self):
        return self._subject
    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def body(self):
        return self._body
    @body.setter
    def body(self, value):
        self._body = value
    @property
    def attachments(self):
        return self._attachments
    @attachments.setter
    def attachments(self, value):
        self._attachments = value
        
    def __str__(self):
        return f"MailDTO(subject={self._subject}, body={self._body}, attachments={self._attachments})"
    
    def render_mail(self, pageDto: PageDTO) -> None:
        """Renders the mail body by replacing placeholders with actual values from PageDTO.

        Args:
            pageDto (PageDTO): The PageDTO object containing the data to replace in the mail body.
        """
        self._body = self._body.replace("[Nom entreprise]", pageDto.nom_entreprise or "")
        self._body = self._body.replace("[Civilité]", pageDto.civilite or "")
        self._body = self._body.replace("[Nom de famille]", pageDto.nom_famille or "")