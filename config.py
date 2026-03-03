import os

class Config:
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_secret_key'
    
class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_secret_key'
    
class ProductionConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_secret_key'
    
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}