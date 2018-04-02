## LOC Challenge AI  

##### a Machine Learning Law Match Maker

This application takes any text input and returns the most similar congressional bills using the machine learning [WMD Similarity Model](https://radimrehurek.com/gensim/similarities/docsim.html#gensim.similarities.docsim.WmdSimilarity) and [Google's 2013 pretrained word embeddings](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit)

## Application Installation

    ⏵ pip3 install --user --upgrade flask
    ⏵ git clone git@github.com:whs2k/loc_challenge_ai.git

## Running

    ⏵ cd loc_challenge_aim
    ⏵ env FLASK_APP=challenge.py flask run


Or shortcut:

    ⏵ make run
    
### Recreate This Work:

1. Scrape GPO data (notebooks/1.0-whs-xmlExtract.ipynb)
2. Save Data as CSV (data/1.3-billTitleSponsors.csv)
3. Build and Train WMD Model (notebooks/1.0-whs-xmlExtract.ipynb)
4. Save Model and Similarity Instance; three files (model/-gitignored-)
5. Install and Run Application
