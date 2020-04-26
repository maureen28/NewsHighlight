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
    get_source_url = base_url.format(category, api_key)
    
    with urllib.request.urlopen(get_source_url) as url
    get_sources_data = url.read()
    get_sources_response = json.loads(get_sources_data)
    
    sources_results = None
    if get_sources_response['results']:
        sources_results_list = get_sources_response['results']
        sources_results = process_results(sources_results_list)
        
    return sources_results
 
def process_results(sources_list):
   '''
    Function  that processes the source result and transform them to a list of Objects
    '''
    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
		description = source_item.get('description')
		url = source_item.get('url')
		category = source_item.get('category')
        name = source_item.get('name')
		country = source_item.get('country')
        language = source_item.get('language')
        
        source_object = Sources( id,description,url,category,name,country,language )
        sources_results.append(source_object)

return sources_results

def get_article(id):
    '''
	Function that processes the articles and returns a list of articles objects
	'''
    get_article_url = articles_url.format(id, api_key)
    with urllib.request.urlopen(get_article_url) as url:
        article_details = url.read()
        articles_results = json.loads(article_details)
        
        article_object = None
        if articles_results['articles']:
			articles_object = process_articles(articles_results['articles'])
      
    return article_object

def process_articles(articles_list):
     '''
    Function  that processes the article result and transform them to a list of Objects
    '''
    articles_object = []
    
    for article_item in articles_list:
        id = article_item.get('id')
        title = article_item.get('title')
        image = article_item.get('image')
        description = article_item.get('description')
        url = article_item.get('url')
        author = article_item.get('author')
		date = article_item.get('date')
  
         if image:
			articles_result = Articles(id,author,title,description,url,image,date)
			articles_object.append(articles_result)	
		
	return articles_object
