import urllib2
from lxml import etree
from bs4 import BeautifulSoup

aucartistmap = {'Banksy':'banksy', 'Andy Warhol':'andy-warhol','Agnes Martin':'agnes-martin', 'Roy Lichtenstein':'roy-lichtenstein','Keith Haring':'keith-haring', 'Pablo Picasso':'pablo-picasso'}

def auction(artist):
	dates = []
	low = []
	high = []
	final = []

	baseurl = 'http://www.artnet.com/artists/' + aucartistmap[artist]
	response = urllib2.urlopen(baseurl+'/recent-auctions')
	html_doc = response.read() 
	soup = BeautifulSoup(html_doc)
	linkdoms = soup.find_all("a", class_="lnk9")
	links = []
	for i in xrange(0, len(linkdoms),2):
		links.append(linkdoms[i]['href'])

	datedoms = soup.find_all("span", class_="font10")
	for i in range(1, len(datedoms), 2):
		if datedoms[i].text.find("Sold:") != -1:
			dates.append(datedoms[i].text[6:])

	print dates

	for i in range(0, len(links)):
		response = urllib2.urlopen(baseurl+links[i])
		html_doc = response.read() 
		soup = BeautifulSoup(html_doc, "lxml")
		est = soup.find_all(id='lotInformation_tblCellEstimateText')
		esttokens = est[0].text.split()
		low.append(int(esttokens[0].replace(",", "")))
		high.append(int(esttokens[2].replace(",", "")))
		sold = soup.find_all(id='lotInformation_tblCellSoldForText')
		soldtokens = sold[0].text.split()
		final.append(int(soldtokens[0].replace(",", "")))

	print low
	print high
	print final
	return [dates, low, high, final] 