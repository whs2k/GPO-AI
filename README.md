## LOC Challenge AI

a Machine Learning Law Match Maker

## Application Installation

    ⏵ pip3 install --user --upgrade flask
    ⏵ git clone git@github.com:mixmastamyk/loc_challenge.git

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
5. Run Application:
