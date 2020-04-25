import os

class Config:
    '''General configuration parent class
    '''
    
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