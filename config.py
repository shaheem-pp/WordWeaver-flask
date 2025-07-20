"""
Configuration for the WordWeaver application.
"""

import os

class Config:
    """
    Base configuration settings.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    """
    Development configuration settings.
    """
    DEBUG = True

class ProductionConfig(Config):
    """
    Production configuration settings.
    """
    pass
