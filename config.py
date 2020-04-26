import os

class Config:
 
    NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/{}?country=us&apiKey={}'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
    EVERYTHING_SEARCH_URL = 'https://newsapi.org/v2/everything?q={}&pageSize={}&apiKey={}'
    NEWS_API_KEY = '7909f08eab26458ca3a3e60718f7949d'
    
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