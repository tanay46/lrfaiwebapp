from flask import Flask
from flask import render_template
import datetime
import pymongo
from pymongo import MongoClient
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
		fbx = artistinfo.get('fbx')
		fby = artistinfo.get('fby')
		fby2 = artistinfo.get('fby2')
		aucx = artistinfo.get('aucx')
		auclow = artistinfo.get('auclow')
		auchigh = artistinfo.get('auchigh')
		aucfinal = artistinfo.get('aucfinal')

		return render_template('dashboard.html', wikix = wikicats, wikiy = wikidata, name = name, gtrendsx = gtrendsx, gtrendsy = gtrendsy, artnet = artnet, arrow = arrow, fbx = fbx, fby = fby, fby2 = fby2, aucx = aucx, auclow = auclow, auchigh = auchigh, aucfinal = aucfinal, artist = artist)
	else:
		return render_template('comingsoon.html', name = artist)

@app.route("/compare/<artist>&<artist2>") # show artist page
def compare(artist, artist2):
	MONGOHQ_URL= "mongodb://tanay:tanay@oceanic.mongohq.com:10049/artists"
	client = MongoClient(MONGOHQ_URL)
	db = client.artists
	collection = db.artists
	artistinfo = collection.find_one({"nameclean": artist})
	artist2info = collection.find_one({"nameclean": artist2})
	if artistinfo and artist2info:
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
		fbx = artistinfo.get('fbx')
		fby = artistinfo.get('fby')
		fby2 = artistinfo.get('fby2')
		aucx = artistinfo.get('aucx')
		auclow = artistinfo.get('auclow')
		auchigh = artistinfo.get('auchigh')
		aucfinal = artistinfo.get('aucfinal')

		wikicats2 = artist2info['wikix']
		for i in range(0, len(wikicats)):
			wikicats2[i] = wikicats[i].encode("ascii","ignore")
		wikidata2 = artist2info['wikiy']
		gtrendsx2= artist2info['googlex']
		for i in range(0, len(gtrendsx)):
			gtrendsx2[i] = gtrendsx[i].encode("ascii","ignore")
		gtrendsy2 = artist2info['googley']
		name2 = artist2info['name']
		artnet2 = artist2info.get('artnet')
		previousrank2 = artnet2[1]
		currentrank2 = artnet2[0]
		arrow2 = "glyphicon-arrow-down"
		artnet2 = artnet2[::-1]
		if previousrank2 > currentrank2:
			arrow = "glyphicon-arrow-up"
		elif previousrank2 == currentrank2:
			arrow = "glyphicon-minus" 
		fbx2 = artist2info.get('fbx')
		fby_2 = artist2info.get('fby')
		fby2_2 = artist2info.get('fby2')
		aucx2 = artist2info.get('aucx')
		auclow2 = artist2info.get('auclow')
		auchigh2 = artist2info.get('auchigh')
		aucfinal2 = artist2info.get('aucfinal')

		return render_template('compare.html', wikix = wikicats, wikiy = wikidata, name = name, gtrendsx = gtrendsx, gtrendsy = gtrendsy, artnet = artnet, arrow = arrow, fbx = fbx, fby = fby, fby2 = fby2, aucx = aucx, auclow = auclow, auchigh = auchigh, aucfinal = aucfinal, artist = artist, wikix2 = wikicats2, wikiy2 = wikidata2, name2 = name2, gtrendsx2 = gtrendsx2, gtrendsy2 = gtrendsy2, artnet2 = artnet2, arrow2 = arrow2, fbx2 = fbx2, fby_2 = fby_2, fby2_2 = fby2_2, aucx2 = aucx2, auclow2 = auclow2, auchigh2 = auchigh2, aucfinal2 = aucfinal2, artist2 = artist2)
	else:
		return render_template('comingsoon.html', name = artist)


# @app.route("/artists/<artist>.pdf") # show artist page
# def get_artist_pdf(artist):
# 	html = get_artist_page(artist)
# 	return Response(create_pdf(html), mimetype='application/pdf')


if __name__ == '__main__':
    app.run(debug = True)