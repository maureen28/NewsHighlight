import os

class Config:
    '''General configuration parent class
    '''
    NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
   	ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
    EVERYTHING_SEARCH_URL = 'https://newsapi.org/v2/everything?q={}&pageSize={}&apiKey={}'
 
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    
    
class ProdConfig:
        '''Production  configuration child class
        '''
        pass
    
class DevConfig:
     '''Development  configuration child class
     '''
     DEBUG = True
     
config_options = {
'development': DevConfig,
'production': ProdConfig
}