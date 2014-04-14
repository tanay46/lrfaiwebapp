import urllib2
import json

dates = ['apr-13', 'may-13', 'jun-13', 'jul-13', 'aug-13', 'sep-13', 'oct-13', 'nov-13', 'dec-13', 'jan-14', 'feb-14', 'mar-14']
fbartistmap = {'Banksy':'banksy', 'Andy Warhol':'andywarholpaintings','Agnes Martin':'Agnes-Martin', 'Roy Lichtenstein':'roylichtenstein1','Keith Haring':'Keith-Haring'}

# Aggregated Facebook location data, sorted by country, about the people who like your Page

def facebook(artist):
	valuestr = ''
	likes = []
	for i in range(0, len(dates)-1):
		req = urllib2.Request("https://graph.facebook.com/" + fbartistmap[artist] + "/insights?since=1-" +dates[i]+ "&until=2-" +dates[i]+ "&access_token=1388859028003148|7ec5645154cf6a5ea978b5e710f784b0")
		response = urllib2.urlopen(req)

		obj = json.loads(response.read())
		dat = obj['data'][0]['values'][0]['value']

		totalfans_0 = 0

		for key, value in dat.items():
			totalfans_0 += value

		print totalfans_0

		req = urllib2.Request("https://graph.facebook.com/" + fbartistmap[artist] + "/insights?since=1-" +dates[i+1]+ "&until=2-" +dates[i+1]+ "&access_token=1388859028003148|7ec5645154cf6a5ea978b5e710f784b0")
		response = urllib2.urlopen(req)

		obj = json.loads(response.read())
		dat = obj['data'][0]['values'][0]['value']

		totalfans_1 = 0

		for key, value in dat.items():
			totalfans_1 += value

		likes.append(int(totalfans_1-totalfans_0));
		#valuestr += str(totalfans_1-totalfans_0) + ', '

	print likes
	return likes


# The number of people sharing stories about your page ('People Talking About This' / PTAT). These stories include liking your Page, posting to your Page's Wall, liking, commenting on or sharing one of your Page posts, answering a Question you posted, RSVPing to one of your events, mentioning your Page, phototagging your Page or checking in at your Place
# Note that currently only the weekly value is in real-time if you set until=now in the request. This metric is deprecated after the deprecate_PTAT migration.

for i in range(0, len(dates)):
	valuestr = ''
	req = urllib2.Request("https://graph.facebook.com/andywarholpaintings/insights/page_storytellers_by_country/days_28?since=1-" +dates[i]+ "&until=2-" +dates[i]+ "&access_token=1388859028003148|7ec5645154cf6a5ea978b5e710f784b0")
	response = urllib2.urlopen(req)

	obj = json.loads(response.read())
	dat = obj['data'][0]['values'][0]['value']

	totalfans = 0

	for key, value in dat.items():
		totalfans += value

	valuestr += str(totalfans) + ', '

print valuestr + ' second'


#print obj['data'][0]['values'][0]['value']['US']
