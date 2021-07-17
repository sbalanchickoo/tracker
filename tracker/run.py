import os
import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)

    try:
        # works on linux
        env = os.environ['ENV']
    except:
        # works on windows
        env = app.config["ENV"]

    if env == "production":
        app.config.from_object(config.ProductionConfig)
    elif env == "development":
        app.config.from_object(config.DevelopmentConfig)

    db = SQLAlchemy(app)
    db.create_all()
    db.init_app(app)
    return db, app