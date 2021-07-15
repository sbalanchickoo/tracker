# Standard library imports
import os


class Config:
    DEBUG = False
    # BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.environ.get('SECRET_KEY') or "b'LJO\xe7\xf7\xfft\xc1\x9cf\xfb\xf6K\xcbn\xdf\xebs)\xe2f\x7f\x03\xa4'"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    DB_NAME = "tracker"
    DB_USERNAME = "postgres"
    DB_PASSWORD = "gt"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@localhost:5432/{DB_NAME}"
    # SQLALCHEMY_DATABASE_URI = "postgresql://postgres:gt@localhost:5432/tracker"


class ProductionConfig(Config):
    DEBUG = True
    DB_NAME = "tracker"
    DB_USERNAME = "postgres"
    DB_PASSWORD = "gt"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@172.30.40.2:5432/{DB_NAME}"

