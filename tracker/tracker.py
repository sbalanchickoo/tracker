import models.grouping as grouping
import models.expense as expense
import run
from flask import Flask, render_template, abort, jsonify, request, redirect, url_for

db, app = run.create_app()




# the decorator turns this function to a view function
# app.route is an attribute of the app object above
@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/subcategory/<int:index>')
def get_grouping(index):
    result_set = grouping.Grouping.query.filter(grouping.Grouping.id == index).first()

    if result_set is not None:
        result = result_set.serialize
        return render_template('grouping.html'
                               , category=result['category']
                               , subcategory=result['subcategory']
                               , index=result['id']
        )
    else:
        return abort(404)


@app.route('/subcategory-list')
def get_all_grouping():
    result_set = grouping.Grouping.query.all()

    if result_set is not None:
        result_set_serialized = [i.serialize for i in result_set]
        ids = [i['id'] for i in result_set_serialized]
        return render_template('all-grouping.html'
                               , groupings=result_set_serialized
                               , ids=ids
                               )
    else:
        return abort(404)


@app.route('/api/subcategory/<int:index>')
def api_get_grouping(index):
    result_set = grouping.Grouping.query.filter(grouping.Grouping.id == index).first()

    if result_set is not None:
        result_set_serialized = result_set.serialize
        return jsonify(result_set_serialized)
    else:
        return abort(404)


@app.route('/api/subcategory-list')
def api_get_all_grouping():
    result_set = grouping.Grouping.query.all()

    if result_set is not None:
        result = [i.serialize for i in result_set]
        return jsonify(result)
    else:
        return abort(404)


@app.route('/add-subcategory', methods=['GET', 'POST'])
def add_grouping():
    if request.method == 'POST':
        new_grouping = grouping.Grouping(category=request.form['category'], subcategory=request.form['subcategory'])
        status = grouping.Grouping.add_grouping(new_grouping)
        if status == 'pass':
            return redirect(url_for('get_all_grouping'))
        else:
            return redirect(url_for('add_grouping'))
    else:
        return render_template('add-grouping.html')


@app.route('/delete-subcategory/<int:index>', methods=['GET', 'POST'])
def delete_grouping(index):
    result_set = grouping.Grouping.query.filter(grouping.Grouping.id == index).first()
    if result_set is not None:
        result_set_serialized = result_set.serialize

        if request.method == 'POST':
            grouping.Grouping.delete_grouping(result_set_serialized)
            return redirect(url_for('get_all_grouping'))
        else:
            return render_template('delete-grouping.html'
                                   , category=result_set_serialized['category']
                                   , subcategory=result_set_serialized['subcategory'])
    else:
        return abort(404)


if __name__ == '__main__':
    app.run()