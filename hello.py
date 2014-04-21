from flask import Flask
from flask import render_template
import datetime
import pymongo
from pymongo import MongoClient
from pdfs import create_pdf
import mimerender
from flask import Response

app = Flask(__name__)

@app.route('/') #show regular home page
def index():
	return render_template('index.html')

@app.route("/dashboard") # show list of artists
def view_dashboard():
	MONGOHQ_URL= "mongodb://tanay:tanay@oceanic.mongohq.com:10049/artists"
	client = MongoClient(MONGOHQ_URL)
	db = client.artists
	collection = db.artists
	artistdict = {}
	for artist in collection.find():
		artistdict[artist['name']] = artist['nameclean']
	return render_template('artistpage.html', artists = artistdict)

@app.route("/artists/<artist>") # show artist page
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
		artnet = artistinfo.get('artnet')
		previousrank = artnet[1]
		currentrank = artnet[0]
		arrow = "glyphicon-arrow-down"
		artnet = artnet[::-1]
		if previousrank > currentrank:
			arrow = "glyphicon-arrow-up"
		elif previousrank == currentrank:
			arrow = "glyphicon-minus" 
		fbx = artistinfo['fbx']
		fby = artistinfo['fby']
		fby2 = artistinfo['fby2']
		aucx = artistinfo['aucx']
		auclow = artistinfo['auclow']
		auchigh = artistinfo['auchigh']
		aucfinal = artistinfo['aucfinal']

		return render_template('dashboard.html', wikix = wikicats, wikiy = wikidata, name = name, gtrendsx = gtrendsx, gtrendsy = gtrendsy, artnet = artnet, arrow = arrow, fbx = fbx, fby = fby, fby2 = fby2, aucx = aucx, auclow = auclow, auchigh = auchigh, aucfinal = aucfinal, artist = artist)
	else:
		return render_template('comingsoon.html', name = artist)

@app.route("/artists/<artist>.pdf") # show artist page
def get_artist_pdf(artist):
	html = get_artist_page(artist)
	return Response(create_pdf(html), mimetype='application/pdf')


if __name__ == '__main__':
    app.run(debug = True)