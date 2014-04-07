import urllib2
import json

dates = ['apr-13', 'may-13', 'jun-13', 'jul-13', 'aug-13', 'sep-13', 'oct-13', 'nov-13', 'dec-13', 'jan-14', 'feb-14', 'mar-14']
valuestr = ''

for i in range(0, len(dates)-1):
	req = urllib2.Request("https://graph.facebook.com/andywarholpaintings/insights?since=1-" +dates[i]+ "&until=2-" +dates[i]+ "&access_token=1388859028003148|7ec5645154cf6a5ea978b5e710f784b0")
	response = urllib2.urlopen(req)

	obj = json.loads(response.read())
	dat = obj['data'][0]['values'][0]['value']

	totalfans_0 = 0

	for key, value in dat.items():
		totalfans_0 += value

	req = urllib2.Request("https://graph.facebook.com/andywarholpaintings/insights?since=1-" +dates[i+1]+ "&until=2-" +dates[i+1]+ "&access_token=1388859028003148|7ec5645154cf6a5ea978b5e710f784b0")
	response = urllib2.urlopen(req)

	obj = json.loads(response.read())
	dat = obj['data'][0]['values'][0]['value']

	totalfans_1 = 0

	for key, value in dat.items():
		totalfans_1 += value

	valuestr += str(totalfans_1-totalfans_0) + ', '

print valuestr

valuestr = ''
for i in range(0, len(dates)):
	req = urllib2.Request("https://graph.facebook.com/andywarholpaintings/insights/page_storytellers_by_country/days_28?since=1-" +dates[i]+ "&until=2-" +dates[i]+ "&access_token=1388859028003148|7ec5645154cf6a5ea978b5e710f784b0")
	response = urllib2.urlopen(req)

	obj = json.loads(response.read())
	dat = obj['data'][0]['values'][0]['value']

	totalfans = 0

	for key, value in dat.items():
		totalfans += value

	valuestr += str(totalfans) + ', '

print valuestr

#print obj['data'][0]['values'][0]['value']['US']
