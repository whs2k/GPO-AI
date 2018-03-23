from __future__ import print_function
from flask import Flask
from flask import redirect, request, url_for
from flask import render_template as render

#~ import patentSimilarityApp
import patentSimilarityApp_sim as patentSimilarityApp


app = Flask(__name__)
patentSimilarityApp.init()


@app.route('/', methods=('GET', 'POST'))
def start_page():

    if request.method == 'POST':

        input_text = request.form.get('input_text')
        # temporary redirect with data for testing purposes
        return redirect(url_for('results_page', input_text=input_text), code=307)
    else:
        return render('start.html')


@app.route('/results/', methods=('GET', 'POST'))
def results_page():

    results = []

    if request.method == 'POST':
        input_text = request.form.get('input_text')

        results = patentSimilarityApp.get_similar_docs(input_text)

    return render('results.html', results=results)
