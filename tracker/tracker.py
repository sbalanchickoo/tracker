from flask import Flask, render_template, abort, jsonify, request, redirect, url_for
from tracker import app
from tracker.model.grouping import Grouping
from sqlalchemy import func

# constructor - pass name of the application
# __name__ is a special variable representing name of current module
# app = Flask(__name__)


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