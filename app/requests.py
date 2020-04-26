import urllib.request, json
from .models import Sources,Articles

# Getting api key
api_key = None

# Getting the base url
base_url = None

# Getting the article
articles_url = None

# search
everything_search_url = None

def configure_request(app):
    global api_key,base_url, articles_url, everything_search_url
    api_key = app.config ['NEWS_API_KEY']
    base_url = app.config ['NEWS_API_BASE_URL']
    articles_url = app.config ['ARTICLES_API_KEY']
    everything_search_url = app.config['EVERYTHING_SEARCH_URL']
    
def get_sources(category):
        '''
    Function that gets the json response to our url request
    '''