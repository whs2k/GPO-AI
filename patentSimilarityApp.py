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
    
    global stop_words, instanceX, df
    stopwords.words('english')

    download('stopwords')
    download('punkt')

    print('Importing Similarity INstance...this will be 65 seconds')
    relPath = 'model/1.1-whs-Sim_Instance'
    absPath = os.path.join(os.getcwd(), relPath)
    instanceX = WmdSimilarity.load(absPath)

    print('Importing Data...')
    relPath = 'data/1.0-billTitleSponsors.csv'
    absPath = os.path.join(os.getcwd(), relPath)
    print(absPath)

    df = pd.read_csv(absPath)
    print('we ready')


def preprocess(doc):

    doc = doc.lower()  # Lower the text.
    doc = word_tokenize(doc)  # Split into words.
    doc = [w for w in doc if not w in stopwords.words('english')]  # Remove stopwords.
    doc = [w for w in doc if w.isalpha()]  # Remove numbers and punctuation.
    return doc

def get_similar_docs(text):
    query = preprocess(text)
    sims = instanceX[query]
    titles = sponsers = texts = []
    for i in range(1):
        #print('sim = %.4f' % sims[i][1])
        titles.append(df.title.values[sims[i][0]])
        sponsers.append(df.sponsers.values[sims[i][0]])
        texts.append(df.texts.values[sims[i][0]])

    return [(titles[0], sponsers[0]),#, texts[0]),
        (titles[1], sponsers[1]),#, texts[0]),
        (titles[2], sponsers[2])]#, texts[0])]


#~ def full_pipeline(input_text):
    #~ ''' Function may be unnecessary. '''

    #~ return get_similar_patents(input_text)


if __name__ == '__main__':
    import sys
    from pprint import pprint

    print('results:\n')
    pprint(get_similar_docs(sys.argv[1], title=sys.argv[2]))


