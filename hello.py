from flask import Flask
from flask import render_template
import datetime
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route("/dashboard")
def view_dashboard():
	MONGOHQ_URL= "mongodb://tanay:tanay@oceanic.mongohq.com:10049/artists"
	client = MongoClient(MONGOHQ_URL)
	db = client.artists
	collection = db.artists
	artistdict = {}
	for artist in collection.find():
		artistdict[artist['name']] = artist['nameclean']
	return render_template('artistpage.html', artists = artistdict)

@app.route("/artists/<artist>")
def get_artist_page(artist):
	MONGOHQ_URL= "mongodb://tanay:tanay@oceanic.mongohq.com:10049/artists"
	client = MongoClient(MONGOHQ_URL)
	db = client.artists
	collection = db.artists
	artistinfo = collection.find_one({"nameclean": artist})
	print artistinfo
	if artistinfo:
		wikicats = artistinfo['wikix']
		for i in range(0, len(wikicats)):
			wikicats[i] = wikicats[i].encode("ascii","ignore")
		wikidata = artistinfo['wikiy']
		gtrendsx = artistinfo['googlex']
		for i in range(0, len(gtrendsx)):
			gtrendsx[i] = gtrendsx[i].encode("ascii","ignore")
		gtrendsy = artistinfo['googley']
		name = artistinfo['name']
		return render_template('dashboard.html', wikix = wikicats, wikiy = wikidata, name = name, gtrendsx = gtrendsx, gtrendsy = gtrendsy)
	else:
		return "We haven't added this artist yet. Coming soon!"


if __name__ == '__main__':
    app.run(debug = True)