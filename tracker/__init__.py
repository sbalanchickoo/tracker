# import os
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from tracker.config import DevelopmentConfig, ProductionConfig
#
# # initialize app
# # constructor - pass name of the application
# # __name__ is a special variable representing name of current module
# app = Flask(__name__)
#
# # env refers to the FLASK_ENV environment variable which can be used to determine config that will be used
# try:
#     # works on linux
#     env = os.environ['ENV']
# except:
#     # works on windows
#     env = app.config["ENV"]
#
# if env == "production":
#     app.config.from_object(ProductionConfig)
# elif env == "development":
#     app.config.from_object(DevelopmentConfig)
#
# # initialize db
# db = SQLAlchemy(app)

# pip list --format=freeze > custom_requirements.txt
# set FLASK_APP=tracker.py
# set FLASK_ENV=development
# flask run

# import model
