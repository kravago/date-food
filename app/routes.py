from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import QueryForm

from yelp_functions import search#, API_KEY
import os
API_KEY = os.environ.get('API_KEY', None)

import random

@app.route('/', methods=['GET', 'POST'])
def index():
    form = QueryForm()
    if form.validate_on_submit():
            flash('Finding {}, in {} with an expensiveness level of {}.'.format(
                form.food_type.data, form.location.data, form.price_range.data))

            # query yelp api
            yelp_results = search(API_KEY, form.food_type.data, form.location.data, form.price_range.data)

            # select random item in list
            rand_restaurant = random.randint(0,10)

            return render_template('results.html', yelp_results=yelp_results['businesses'][rand_restaurant])

    return render_template('index.html', form=form)