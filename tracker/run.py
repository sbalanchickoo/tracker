import os
import config
from flask import Flask


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

    from models import db
    db.init_app(app)

    return app