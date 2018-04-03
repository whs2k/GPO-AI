from __future__ import print_function
import atexit
import csv
import os
from datetime import datetime
from collections import deque
from concurrent.futures import ThreadPoolExecutor # ProcessPoolExecutor

from flask import Flask
from flask import redirect, request, url_for
from flask import render_template as render

import config
if os.environ.get('LOC_SIM'):
    import patentSimilarityApp_sim as patentSimilarityApp
else:
    import patentSimilarityApp


# Poor man's job queue
executor = ThreadPoolExecutor(config.num_threads)
jobs = deque(maxlen=config.job_list_capacity)

app = Flask(__name__)
patentSimilarityApp.init()
log_file = open(config.query_log_filename, 'a')
query_log = csv.writer(log_file)


#~ import signal; signal.signal(signal.SIGINT, _cleanup)
@atexit.register
def _cleanup():
    ''' Shutdown gracefully.
        Doesn't work with Ctrl-C SIGINT vs. threading, unsolved.
    '''
    print('\nbye')
    executor.shutdown()
    log_file.close()


@app.route('/', methods=('GET', 'POST'))
def start_page():

    if request.method == 'POST':
        input_text = request.form.get('input_text')

        # record query
        timestamp = datetime.now().isoformat()
        query_log.writerow((timestamp,
                            input_text.replace('\r\n', ' ')) )  # rm CRLF
        log_file.flush()  # slower but ensures full log when interrupted

        job = executor.submit(patentSimilarityApp.get_similar_docs, input_text)
        # save name for later summary view:
        job._name = input_text[:config.view_query_summarize_length]
        job._timestamp = timestamp.partition('.')[0].replace('T', ' ')
        jobs.append(job)
        return redirect(url_for('jobs_page'), code=303)  # as GET
    else:
        return render('start.html')


@app.route('/jobs')
def jobs_page():

    return render('jobs.html', results=jobs, config=config)


@app.route('/results/<int:index>')
def result_page(index):
    try:
        job = jobs[index]
        jobname = job._name
        timestamp = job._timestamp
        results = job.result()
    except IndexError:
        jobname = timestamp = ''
        results = ('Nothing found.', '', '')

    return render('results.html',
                  results=results, index=index, jobname=jobname,
                  timestamp=timestamp,
                  sponlimit=config.view_results_sponsor_limit)
