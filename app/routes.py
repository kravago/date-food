from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import QueryForm

from yelp_functions import search
import os
API_KEY = os.environ.get('API_KEY', None)

import random

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = QueryForm()

    # form submission actions
    if form.validate_on_submit():
            # query yelp api
            yelp_results = search(API_KEY, form.food_type.data, form.location.data)
            total = len(yelp_results['businesses'])

            # if no results, redirect to error page
            if total==0:
                return render_template('sorry.html')
            else:
                rand_restaurant = random.randint(0, total-1)
                return render_template('results.html', yelp_results=yelp_results['businesses'][rand_restaurant])

    return render_template('index.html', form=form)