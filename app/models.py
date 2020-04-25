class Sources:
    """ Sources to define news source objects
    """
    def __init__(self, id, description, url, category, name, country, language ):   
        """Create instances for newsSource
        """
        self.id = id
        self.description = description
        self.url = url
        self.category = category
        self.name = name
        self.country = country
        self.language = language