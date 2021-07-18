# from tracker.py

# from datetime import datetime

# @app.route('/visitor-count')
# def count():
#     global counter
#     counter += 1
#     return 'This page has been visited ' + str(counter) + ' time/(s)'
#
#
# @app.route('/date')
# def date():
#     return "This page was served at " + str(datetime.now())


# if __app__ == '__main__':
#   app.run()
# set FLASK_APP=tracker.py
# set FLASK_ENV=development
# flask run
# python -m flask run
# conda env export > environment.yml

# @app.route('/grouping')
# def grouping():
#     subcategory = 'Mortgage'
#
#     # Option 1
#     # grouping_set = Grouping.query.filter_by(subcategory=subcategory)
#     # returns = list(grouping_set)
#
#     # Option 2
#     # grouping_set = Grouping.query.filter_by(subcategory=subcategory).all()
#
#     # result = [i.serialize for i in returns][0]
#
#     # returns = list(grouping_set)
#     # result = [i.serialize for i in returns][0]
# @app.route('/grouping/<string:subcategory>')
# subcategory = subcategory.lower()
#     grouping_set = Grouping.query.filter(func.lower(Grouping.subcategory) == subcategory).first()

# import os
# >>> os.urandom(24)










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


#

#