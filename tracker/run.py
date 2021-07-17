# import os
# import config
# # from config import DevelopmentConfig, ProductionConfig
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
#
# db = SQLAlchemy()
#
#
#
# def create_app(config_name):
#     app = Flask(__name__)
#
#     try:
#         # works on linux
#         env = os.environ['ENV']
#     except:
#         # works on windows
#         env = app.config["ENV"]
#
#     if env == "production":
#         app.config.from_object(config.ProductionConfig)
#     elif env == "development":
#         app.config.from_object(config.DevelopmentConfig)
#
#     # app.config.from_object(config[config_name])
#     db = SQLAlchemy(app)
#     db.create_all()
#     db.init_app(app)
#     return app
