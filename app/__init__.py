"""
Initializes the Flask application.
"""

from flask import Flask
from config import DevelopmentConfig

def create_app(config_class=DevelopmentConfig):
    """
    Creates and configures the Flask application.

    Args:
        config_class: The configuration class to use.

    Returns:
        The Flask application instance.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    with app.app_context():
        from . import routes

    return app
