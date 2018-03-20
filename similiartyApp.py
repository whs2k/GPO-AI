from __future__ import print_function
from datetime import datetime
import numpy as np

import pandas as pd
import time
from time import time
import os

import os
import gensim
from gensim.models import Word2Vec, KeyedVectors
from gensim.similarities import WmdSimilarity

from nltk.corpus import stopwords
from nltk import download
from nltk import word_tokenize

def init():
	print('Initializing...')

	stop_words = stopwords.words('english')
	download('punkt')

	relPath = 'model/1.1-whs-Sim_Instance'
	absPath = os.path.join(os.path.dirname(os.getcwd()), relPath)
	instanceX = WmdSimilarity.load(absPath)

	relPath = 'data/1.0-billTitleSponsors.csv'
	absPath = os.path.join(os.path.dirname(os.getcwd()), relPath)

	df = pd.read_csv(absPath)

def preprocess(doc):
    doc = doc.lower()  # Lower the text.
    doc = word_tokenize(doc)  # Split into words.
    doc = [w for w in doc if not w in stop_words]  # Remove stopwords.
    doc = [w for w in doc if w.isalpha()]  # Remove numbers and punctuation.
    return doc

def get_similar_docs(text):
	query = preprocess(text)
	sims = instanceX[query]
	titles = sponsers = []
	for i in range(3):
	    #print('sim = %.4f' % sims[i][1])
	    titles.append(df.title.values[sims[i][0]])
	    sponsers.append(df.sponsers.values[sims[i][0]])

	return [(titles[0], sponsers[0]),
		(titles[1], sponsers[1]),
		(titles[2], sponsers[2])]

if __name__ == '__main__':
    import sys
    from pprint import pprint

    print('results:\n')
    pprint(get_similar_patents(sys.argv[1], title=sys.argv[2]))
