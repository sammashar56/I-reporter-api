import os

class Config:
    """Parent configuration class."""
    DEBUG = False
    
class Testing(Config):
    """configuration for testing"""
    DEBUG = True

class Development(Config):
    """configuration for development"""
    DEBUG = True


app_config = {
    'development':Development,
    'testing': Testing,
}
