from __future__ import print_function
#~ import os
import atexit
from concurrent.futures import ThreadPoolExecutor # ProcessPoolExecutor

from flask import Flask
from flask import redirect, request, url_for
from flask import render_template as render

#~ import patentSimilarityApp
import patentSimilarityApp_sim as patentSimilarityApp

# poor man's job queue
executor = ThreadPoolExecutor(2)
atexit.register(lambda: print('\nbye'))
atexit.register(lambda: executor.shutdown())
jobs = []

app = Flask(__name__)
patentSimilarityApp.init()


@app.route('/', methods=('GET', 'POST'))
def start_page():

    if request.method == 'POST':
        input_text = request.form.get('input_text')
        jobs.append(
            executor.submit(patentSimilarityApp.get_similar_docs, input_text)
        )
        return redirect(url_for('jobs_page'), code=303)  # as GET
    else:
        return render('start.html')


@app.route('/jobs')
def jobs_page():

    return render('jobs.html', results=jobs)


@app.route('/results/<int:index>')
def result_page(index):
    try:
        results = jobs[index].result()
    except IndexError:
        results = ('Nothing found.', '', '')

    return render('results.html', results=results)
