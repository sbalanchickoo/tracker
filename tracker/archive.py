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