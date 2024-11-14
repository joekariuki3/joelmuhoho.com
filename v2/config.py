import os
from dotenv import load_dotenv
import base64

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', base64.b64encode(os.urandom(24)).decode('utf-8'))
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///portfolio.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # root user info
    ROOT_FIRST_NAME=os.getenv('ROOT_FIRST_NAME')
    ROOT_LAST_NAME=os.getenv('ROOT_LAST_NAME')
    ROOT_EMAIL=os.getenv('ROOT_EMAIL')
    ROOT_PASSWORD=os.getenv('ROOT_PASSWORD')

    DEFAULT_PROFILE_IMAGE_URL=os.getenv('DEFAULT_PROFILE_IMAGE_URL')

class DevelopmentConfig(Config):
    DEBUG = True
    SERVER_HOST = '0.0.0.0'

class ProductionConfig(Config):
    DEBUG = False
    SERVER_HOST = '127.0.0.1'