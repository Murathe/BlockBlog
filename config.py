# import os





# class Config:
#     debug = True
#     SECRET_KEY = os.environ.get('SECRET_KEY')
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mutumas:Mutuma1234@localhost/blocpost'


#     #  email configurations
#     MAIL_SERVER = 'smtp.gmail.com'
#     MAIL_PORT = 465
#     MAIL_USE_TLS = False
#     MAIL_USE_SSL = True
#     MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
#     MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

# class ProdConfig(Config):
#     '''
#     Production  configuration child class

#     Args:
#         Config: The parent configuration class with General configuration settings
#     '''
#     SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

# class TestConfig(Config):
#     '''
#     Testing configuration child class
#     Args:
#         Config: The parent configuration class with General configuration settings
#     '''
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mutumas:Mutuma1234@localhost/blocpost'

# class DevConfig(Config):
#     '''
#     Development  configuration child class

#     Args:
#         Config: The parent configuration class with General configuration settings
#     '''

#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mutumas:Mutuma1234@localhost/blocpost'

    
    
#     DEBUG = True
#     ENV = 'development'

# config_options = {    
#     'development':DevConfig,
#     'production':ProdConfig,
#     'test':TestConfig
# }
import os

class Config:
    '''
    General configuration class
    '''
    debug = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # WTF_CSRF_SECRET_KEY= os.environ.get('WTF_CSRF_SECRET_KEY')
    SECRET_KEY='brian'
    # WTF_CSRF_SECRET_KEY='secret'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mutumas:Mutuma1234@localhost/blocpost'
    

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    

    # QUOTES_URL = 'http://quotes.stormconsultancy.co.uk/random.json'

class ProdConfig(Config):
    '''
    Production  configuration class
    '''
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    

class TestConfig(Config):
    '''
    Testing configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mutumas:Mutuma1234@localhost/blocpost'

    
class DevConfig(Config):
    '''
    Development  configuration class
    '''
    
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://mutumas:Mutuma1234@localhost/blocpost'

    DEBUG= True
    ENV = 'development'
    
config_options = {
    'production' : ProdConfig,
    'development' : DevConfig,
    'test': TestConfig
}
