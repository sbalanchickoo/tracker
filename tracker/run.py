import os
import config
import models.grouping as grouping
import models.expense as expense

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
    # import models objects (above) so that they will be created if not already exist
    # even though lines are greyed out, they are essential, so that the db objects knows of the models objects
    import models.grouping as grouping
    import models.expense as expense
    db.create_all()
    db.session.commit()
    return db, app