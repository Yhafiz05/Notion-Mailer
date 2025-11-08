class PageDTO:
    """
    PageDTO is a Data Transfer Object (DTO) that represents a page with various attributes.

    Attributes:
        id (str): The unique identifier of the page.
        etape (str): The step or stage associated with the page.
        secteur (str): The sector or domain related to the page.
        email (str): The email address associated with the page.
        civilite (str): The civility or title (e.g., Mr., Ms.) of the person related to the page.
        date_candidature (str): The date of the application or candidacy associated with the page.
    """
    def __init__(
        self, id: str | None,
        etape: str | None,
        secteur: list[str | None],
        nom_entreprise: str | None,
        email: str | None,
        civilite: list[str | None],
        nom_famille: str | None,
        date_canditature: str | None
    ):
        self._id = id
        self._etape = etape
        self._secteur = secteur
        self._nom_entreprise = nom_entreprise
        self._email = email
        self._civilite = civilite
        self._nom_famille = nom_famille
        self._date_candidature = date_canditature

    # Getter and Setter for id
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    # Getter and Setter for etape
    @property
    def etape(self):
        return self._etape

    @etape.setter
    def etape(self, value):
        self._etape = value

    # Getter and Setter for secteur
    @property
    def secteur(self):
        return self._secteur

    @secteur.setter
    def secteur(self, value):
        self._secteur = value

    # Getter and Setter for email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    # Getter and Setter for civilite
    @property
    def civilite(self):
        return self._civilite

    @civilite.setter
    def civilite(self, value):
        self._civilite = value

    # Getter and Setter for date_candidature
    @property
    def date_candidature(self):
        return self._date_candidature

    @date_candidature.setter
    def date_candidature(self, value):
        self._date_candidature = value
        
    @property
    def nom_entreprise(self):
        return self._nom_entreprise
    
    @nom_entreprise.setter
    def nom_entreprise(self, value):
        self._nom_entreprise = value
    
    @property
    def nom_famille(self):
        return self._nom_famille
    @nom_famille.setter
    def nom_famille(self, value):
        self._nom_famille = value
        
    def __str__(self):
        return f"PageDTO(id={self._id}, etape={self._etape}, secteur={self._secteur}, nom_entreprise={self._nom_entreprise}, email={self._email}, civilite={self._civilite}, nom_famille={self._nom_famille}, date_candidature={self._date_candidature})"