import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from tracker.config import DevelopmentConfig, ProductionConfig
import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))

# initialize app
# constructor - pass name of the application
# __name__ is a special variable representing name of current module
app = Flask(__name__)

# env refers to the FLASK_ENV environment variable which can be used to determine config that will be used
try:
    env = os.environ['ENV']
except:
    env = app.config["ENV"]
# if app.config["ENV"] == "production":
if env == "production":
    app.config.from_object(ProductionConfig)
elif env == "development":
    app.config.from_object(DevelopmentConfig)

# initialize db
db = SQLAlchemy(app)

# pip list --format=freeze > custom_requirements.txt

# db = SQLAlchemy()
