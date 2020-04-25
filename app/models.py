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
        
        
class Articles:
    """ Articles class to define news Article objects
    """
    def __init__(self, id, title, image, description, url, author,  date):
        """Create instances for newsArticle
        """
        self.id = id
        self.title = title
        self.image = image
        self.description = description
        self.url = url
        self.author = author
        self.date = date
        