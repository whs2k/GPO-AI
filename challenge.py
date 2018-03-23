from __future__ import print_function
import atexit
from concurrent.futures import ThreadPoolExecutor # ProcessPoolExecutor

from flask import Flask
from flask import redirect, request, url_for
from flask import render_template as render

#~ import patentSimilarityApp
import patentSimilarityApp_sim as patentSimilarityApp
import config


# Poor man's job queue
executor = ThreadPoolExecutor(config.num_threads)
atexit.register(lambda: print('\nbye'))
atexit.register(lambda: executor.shutdown())
jobs = []

app = Flask(__name__)
patentSimilarityApp.init()


@app.route('/', methods=('GET', 'POST'))
def start_page():

    if request.method == 'POST':
        input_text = request.form.get('input_text')
        job = executor.submit(patentSimilarityApp.get_similar_docs, input_text)
        job._name = input_text[:8]  # save for later
        jobs.append(job)
        return redirect(url_for('jobs_page'), code=303)  # as GET
    else:
        return render('start.html')


@app.route('/jobs')
def jobs_page():

    return render('jobs.html', results=jobs)


@app.route('/results/<int:index>')
def result_page(index):
    try:
        job = jobs[index]
        jobname = job._name
        results = job.result()
    except IndexError:
        jobname = ''
        results = ('Nothing found.', '', '')

    return render('results.html',
                  results=results, index=index, jobname=jobname)
