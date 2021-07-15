from flask import Flask, render_template, abort, jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# from tracker.model.grouping import Grouping
from ..model.grouping import Grouping
from .. import app, db
# import os #
# from config import DevelopmentConfig, ProductionConfig #

# app = Flask(__name__) #
# try: #
#     env = os.environ['ENV'] #
# except: #
#     env = app.config["ENV"] #
# if env == "production": #
#     app.config.from_object(ProductionConfig) #
# elif env == "development": #
#     app.config.from_object(DevelopmentConfig) #
# db = SQLAlchemy(app) #

# import model objects so that they will be created if not already exist
# even though below line is greyed out, it is essential, so that the db objects knows of the model objects
# from  import grouping, expense
db.create_all()
db.session.commit()


# the decorator turns this function to a view function
# app.route is an attribute of the app object above
@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/subcategory/<int:index>')
def get_grouping(index):
    grouping = Grouping.query.filter(Grouping.id == index).first()

    if grouping is not None:
        result = grouping.serialize
        return render_template('grouping.html'
                               , category=result['category']
                               , subcategory=result['subcategory']
                               , index=result['id']
        )
    else:
        return abort(404)


@app.route('/subcategory-list')
def get_all_grouping():
    grouping = Grouping.query.all()

    if grouping is not None:
        result = [i.serialize for i in grouping]
        ids = [i['id'] for i in result]
        return render_template('all-grouping.html'
                               , groupings=result
                               , ids=ids
                               )
    else:
        return abort(404)


@app.route('/api/subcategory/<int:index>')
def api_get_grouping(index):
    grouping = Grouping.query.filter(Grouping.id == index).first()

    if grouping is not None:
        result = grouping.serialize
        return jsonify(result)
    else:
        return abort(404)


@app.route('/api/subcategory-list')
def api_get_all_grouping():
    grouping = Grouping.query.all()

    if grouping is not None:
        result = [i.serialize for i in grouping]
        return jsonify(result)
    else:
        return abort(404)


@app.route('/add-subcategory', methods=['GET', 'POST'])
def add_grouping():
    if request.method == 'POST':
        new_grouping = Grouping(category=request.form['category'], subcategory=request.form['subcategory'])
        status = Grouping.add_grouping(new_grouping)
        if status == 'pass':
            return redirect(url_for('get_all_grouping'))
        else:
            return redirect(url_for('add_grouping'))
    else:
        return render_template('add-grouping.html')


@app.route('/delete-subcategory/<int:index>', methods=['GET', 'POST'])
def delete_grouping(index):
    grouping = Grouping.query.filter(Grouping.id == index).first()
    if grouping is not None:
        result = grouping.serialize

        if request.method == 'POST':
            Grouping.delete_grouping(grouping)
            return redirect(url_for('get_all_grouping'))
        else:
            return render_template('delete-grouping.html'
                                   , category=result['category']
                                   , subcategory=result['subcategory'])
    else:
        return abort(404)

# set FLASK_APP=tracker.py
# set FLASK_ENV=development
# flask run