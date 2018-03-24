from __future__ import print_function
import os

import pandas as pd
from gensim.similarities import WmdSimilarity

from nltk.corpus import stopwords
from nltk import download
from nltk import word_tokenize

instanceX = df = None


def init():
    print('Initializing...')

    global instanceX, df
    stopwords.words('english')

    download('stopwords')
    download('punkt')

    print('Importing Similarity Instance...this will be 65 seconds')
    relPath = 'model/1.2-whs-Sim_Instance'
    absPath = os.path.join(os.getcwd(), relPath)
    instanceX = WmdSimilarity.load(absPath)

    print('Importing Data...')
    relPath = 'data/1.3-billTitleSponsors.csv'
    absPath = os.path.join(os.getcwd(), relPath)
    print(absPath)

    df = pd.read_csv(absPath)
    df = df.dropna()
    print('we ready')


def preprocess(doc):

    doc = doc.lower()           # Lower the text.
    doc = word_tokenize(doc)    # Split into words.

    doc = [ w for w in doc
            if not w in stopwords.words('english')
            if w.isalpha() ]    # Filter stopwords, numbers and punctuation
    return doc


def get_similar_docs(text):
    query = preprocess(text)
    sims = instanceX[query]
    titles = []
    sponsors = []
    urls = []
    texts = []
    for i in range(3):
        #print('sim = %.4f' % sims[i][1])
        title = df.title.values[sims[i][0]]
        url = str(df.url.values[sims[i][0]])
        text = df.texts.values[sims[i][0]]

        titles.append(title)
        sponsors.append(df.sponsers.values[sims[i][0]])
        texts.append(text)
        urls.append(url)
        #print(titles)#, sponsors)
    return [
        (sponsors[0], titles[0], urls[0], texts[0]),#, urls[0]), #, texts[0]),
        (sponsors[1], titles[1], urls[1], texts[1]),#, urls[1]), #, texts[0]),
        (sponsors[2], titles[2], urls[2], texts[2])#, urls[2]), #, texts[0]),
    ]


if __name__ == '__main__':
    import sys
    from pprint import pprint

    print('results:\n')
    pprint(get_similar_docs(sys.argv[1], title=sys.argv[2]))


