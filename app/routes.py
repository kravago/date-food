from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import QueryForm

@app.route('/', methods=['GET', 'POST'])
def index():
    form = QueryForm()
    if form.validate_on_submit():
            flash('Finding {}, in {} with an expensiveness level of {}'.format(
                form.food_type.data, form.location.data, form.price_range.data))
            return redirect(url_for('results'))
    return render_template('index.html', form=form)

@app.route('/results')
def results():
    return render_template('results.html')