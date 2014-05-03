import urllib
import re
from pyGTrends import pyGTrends
import csv, datetime, time, getpass, sys
import json
import os
import datetime
import pymongo
from pymongo import MongoClient
import csv
import urllib2
from lxml import etree
from bs4 import BeautifulSoup


# use this file to put data into the mongo database
class ArtData:

  def __init__(self):
    self.MONGOHQ_URL= "mongodb://tanay:tanay@oceanic.mongohq.com:10049/artists"

  def start(self):
    artists = open("artists.txt", 'rw')
    listofart = []
    for line in artists:
      line = line.strip()
      listofart.append(line)
    print listofart
    for name in listofart[5:25]:
      self.makeartist(name)

  def makeartist(self, artistname):
    client = MongoClient(self.MONGOHQ_URL)
    db = client.artists
    collection = db.artists
    artnetr = self.getArtnet(artistname)
    fb = self.facebook(artistname)
    auc = self.auction(artistname)

    artist = collection.find_one({"name": artistname})
    if artist:
      if not artist.get("artnet"):
        collection.update({'name': artistname},
           {
              '$set': { 'artnet': artnetr}
           }
        )
      if 1:#not artist.get("fbx"):
        collection.update({'name': artistname},
           {
              '$set': { 'fbx': fb[0], 'fby': fb[1], 'fby2': fb[2]}
           }
        )
      if 1:#not artist.get("aucx"):
        collection.update({'name': artistname},
           {
              '$set': { 'aucx': auc[0], 'auclow': auc[1], 'auchigh': auc[2], 'aucfinal': auc[3]}
           }
        )
      if not artist.get("wikix"):
        wiki = self.wikipedia(artistname)
        wikix = wiki[1]
        wikiy = wiki[0]
        collection.update({'name': artistname},
           {
              '$set': { 'wikix': wikix, 'wikiy': wikiy}
           }
        )
      if not artist.get("googlex"):
        googletrends = self.googletrends(artistname)
        gtrendsx = googletrends[0]
        gtrendsy = googletrends[1]
        collection.update({'name': artistname},
           {
              '$set': { 'googlex': gtrendsx, 'googley': gtrendsy}
           }
        )
    else:
      wiki = self.wikipedia(artistname)
      wikix = wiki[1]
      wikiy = wiki[0]
      instagram = self.instagram(artistname)
      googletrends = self.googletrends(artistname)
      gtrendsx = googletrends[0]
      gtrendsy = googletrends[1]
      fb = self.facebook(artistname)
      fbx = fb[0]
      fby = fb[1]
      fby2 = fb[2]
      auc = self.auction(artistname)
      aucx = auc[0]
      auclow = auc[1]
      auchigh = auc[2]
      aucfinal = auc[3]

      nameclean = artistname.replace(" ", "").lower()
      artist = {"name": artistname,
                "nameclean" : nameclean,
                "wikix" : wikix,
                "wikiy" : wikiy,
                "instagram" : instagram,
                "googlex" : gtrendsx,
                "googley" : gtrendsy,
                "artnet" : artnetr,
                "fbx" : fbx,
                "fby" : fby,
                "fby2" : fby2,
                "aucx" : aucx,
                "auclow" : auclow,
                "auchigh" : auchigh,
                "aucfinal" : aucfinal
                }
      artist_id = collection.insert(artist)
      print artist_id

  def wikipedia(self, artistname):
    # Get a file-like object for the Python Web site's home page.
    values = []
    months = []
    wiki = {}
    for i in range(1,13):
      if i < 10:
        yearmonth = "20130" + str(i)
      else:
        yearmonth = "2013" + str(i)
      website = "http://stats.grok.se/en/" + yearmonth + "/" + artistname 
      f = urllib.urlopen(website)
      s = f.read()
      regex = re.compile("has been viewed (\d*)")
      r = regex.search(s)
      wiki[yearmonth] = int(r.groups()[0])
      values.append(int(r.groups()[0]))
      months.append(yearmonth)
      f.close()
    for i in range(1,4):  
      yearmonth = "20140" + str(i)
      website = "http://stats.grok.se/en/" + yearmonth + "/" + artistname 
      f = urllib.urlopen(website)
      s = f.read()
      regex = re.compile("has been viewed (\d*)")
      r = regex.search(s)
      wiki[yearmonth] = int(r.groups()[0])
      values.append(int(r.groups()[0]))
      months.append(yearmonth)
      f.close()
    print "finished wiki"
    return [values, months]
    # print values
    # print months

  def googletrends(self, artistname):
    return self.getGTData(artistname)

  def instagram(self, artistname):
    clientid = "d88fc4bf02b84531b4b908d806d1c101" 
    namenospace = artistname.replace(' ', '')
    url = "https://api.instagram.com/v1/tags/"+ namenospace + "?client_id=" + clientid
    f = urllib.urlopen(url)
    s = f.read()
    try:
      x = json.loads(s)
    except:
      return 0
    else:
      return 0
    if x['meta']['code'] == 200:
      number = x['data']['media_count']
      print "finished insta"
      return number
    else:
      return 0

  def getArtnet(self, artistname):
    rankings = open("artnet.csv", 'rU')
    x = rankings.readlines()
    for line in x:
      ld = line.split(",")
      if ld[0] == artistname:
        ld[-1] = ld[-1].strip()
        ld = [ int(x) for x in ld[1:] ]
        print ld
        return ld
    print "oops"

  def getGTData(self, search_query = "debt", date="all", geo="all", scale="1", position = "end" ):
    print search_query
    dict = {}
    endlist = []
    countlist = []
    connector = pyGTrends( "larotondeapi", "dstegroup11")
    connector.download_report( ( search_query ) 
           , date = date
                             , geo = geo
                             , scale = scale )

      #connector.writer()
    # print connector.getData()
    d = csv.DictReader( connector.getData().split('\n'))
    x = connector.csv( section='Main', as_list=True )
    for item in x:
      date = item[0]
      if " - " in date:
        enddate = date.split(" ")[2]
        if (len(item[1])>0):
          try:
            count = int(item[1])
            dict[enddate] = count
            endlist.append(enddate[5:])
            countlist.append(count)
          except:
            break
      elif "-" in date:
        if (len(item[1])>0):
          try:
            count = int(item[1])
            dict[date] = count
            endlist.append(date)
            countlist.append(count)
          except:
            break
    print dict
    return [endlist[-52:], countlist[-52:]]

  def auction(self, artist):
    joan = 'joan-mir%%C3%%B3'
    aucartistmap = {'Banksy':'banksy', 'Andy Warhol':'andy-warhol','Agnes Martin':'agnes-martin', 
    'Roy Lichtenstein':'roy-lichtenstein','Keith Haring':'keith-haring', 'Marc Chagall':'marc-chagall',
    'Carrie Mae Weems':'carrie+mae-weems','Karl Schmidt-Rottluff':'karl-schmidt-rottluff','Andreas Gursky':'andreas-gursky',
    'Louise Lawler':'louise-lawler','Robert Mapplethorpe':'robert-mapplethorpe','Jean-Michel Basquiat':'jean-michel-basquiat',
    'Alexander Calder':'alexander-calder','Pablo Picasso':'pablo-picasso','Joan Miro':joan,
    'Michael Dweck':'michael-dweck','Victor Vasarely':'victor-vasarely','Maurice Utrillo':'maurice-utrillo',
    'Damien Hirst':'damien-hirst'}

    if artist in aucartistmap:
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
          dates.append((datedoms[i].text[6:]).encode('ascii'))

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

    print "finished auction"
    return [dates, low, high, final] 

  def facebook(self, artist):
    dates = ["apr-13", "may-13", "jun-13", "jul-13", "aug-13", "sep-13", "oct-13", "nov-13", "dec-13", "jan-14", "feb-14", "mar-14"]
    fbartistmap = {'Banksy':'banksy', 'Andy Warhol':'andywarholpaintings','Agnes Martin':'Agnes-Martin',
     'Roy Lichtenstein':'roylichtenstein1','Keith Haring':'Keith-Haring', 'Marc Chagall':'Marc-Chagall',
     'Carrie Mae Weems':'CarrieMaeWeems','Karl Schmidt-Rottluff':'Karl-Schmidt-Rottluff','Andreas Gursky':'Andreas-Gursky',
     'Louise Lawler':'Louise-Lawler','Robert Mapplethorpe':'Robert-Mapplethorpe','Jean-Michel Basquiat':'mrjeanmichelbasquiat',
     'Alexander Calder':'Alexander-Calder','Pablo Picasso':'Pablo-Picasso','Joan Miro':'Joan-Miro',
     'Michael Dweck':'Michael-Dweck','Victor Vasarely':'Victor-Vasarely','Maurice Utrillo':'Maurice-Utrillo',
     'Damien Hirst':'Damien-Hirst'}
    valuestr = ''
    likes = []
    interactions = []

    if artist in fbartistmap:
      for i in range(0, len(dates)-1):
        # Aggregated Facebook location data, sorted by country, about the people who like your Page
        #req = urllib2.Request("https://graph.facebook.com/" + fbartistmap[artist] + "/insights?since=1-" +dates[i]+ "&until=2-" +dates[i]+ "&access_token=1388859028003148|7ec5645154cf6a5ea978b5e710f784b0")
        #response = urllib2.urlopen(req)

        req = "https://graph.facebook.com/" + fbartistmap[artist] + "/insights?since=1-" +dates[i]+ "&until=2-" +dates[i]+ "&access_token=1388859028003148|7ec5645154cf6a5ea978b5e710f784b0"
        response = urllib.urlopen(req)

        obj = json.loads(response.read())
        
        if obj['data'] and obj['data'][0] and obj['data'][0]['values'] and obj['data'][0]['values'][0] and obj['data'][0]['values'][0]['value']:
          dat = obj['data'][0]['values'][0]['value'] 
          totalfans_0 = 0
          for key, value in dat.items():
            totalfans_0 += value
          
          req = urllib2.Request("https://graph.facebook.com/" + fbartistmap[artist] + "/insights?since=1-" +dates[i+1]+ "&until=2-" +dates[i+1]+ "&access_token=1388859028003148|7ec5645154cf6a5ea978b5e710f784b0")
          response = urllib2.urlopen(req)
          obj = json.loads(response.read())
          if obj['data'] and obj['data'][0] and obj['data'][0]['values'] and obj['data'][0]['values'][0] and obj['data'][0]['values'][0]['value']:
            dat = obj['data'][0]['values'][0]['value']
            totalfans_1 = 0
            for key, value in dat.items():
              totalfans_1 += value
            likes.append(int(totalfans_1-totalfans_0))
          else:
            likes.append(None)
        else:
            likes.append(None)

      for i in range(0, len(dates)):
        valuestr = ''
        req = urllib2.Request("https://graph.facebook.com/"+ fbartistmap[artist] +"/insights/page_storytellers_by_country/days_28?since=1-" +dates[i]+ "&until=2-" +dates[i]+ "&access_token=1388859028003148|7ec5645154cf6a5ea978b5e710f784b0")
        response = urllib2.urlopen(req)

        obj = json.loads(response.read())
        if obj['data'] and obj['data'][0] and obj['data'][0]['values'] and obj['data'][0]['values'][0] and obj['data'][0]['values'][0]['value']:
          dat = obj['data'][0]['values'][0]['value']
          totalfans = 0
          if dat:
            for key, value in dat.items():
              totalfans += value
            interactions.append(int(totalfans))
        else:
          likes.append(None)      

    print "finished fb"
    return [dates, likes, interactions]


      # data = connector.csv( section='Main' ).split('\n')
      # csv_reader = csv.reader( data )
     #    # example using City to cache search terms
     #    #csv_reader = csv.reader( connector.csv( section='City' ).split('\n') )
     
     #    #for row in csv_reader:
     #    #    print row

     #    #data1 = read_csv_data( data )
     #    #print data1

     #    csv_reader = csv.reader( data )
     #    #fields = csv_reader.next() # Read the column names

     #    # remove all whitespaces
     #    search_query = search_query.strip() 
     #    search_query = " ".join( search_query.split() )
     #    search_query = search_query.replace(" ", "") 
            
     #    with open( search_query + '_google_report.csv', 'w') as csv_out:
     #        positionInWeek = { "start" : 0, "end" : 1 }
     #        separator = " - "
     #        csv_writer = csv.writer( csv_out )
     #        #print "LOOPING ON ENTRIES"
     #        for count, row in enumerate( csv_reader ):
      #     if separator not in row[0] : 
     #                csv_writer.writerow( row )
     #                continue

     #            date = row[0].split( separator )[ positionInWeek[ position ] ] 

      #     # we want to remove any whitespaces from the value entry since we are not interested in blank data points
     #            val = re.sub(r'\s+', '', row[1] )
     #            if len(val) < 1 :
     #                #print "We will skip Null value at date %s" % str(date)
     #                continue
     #            #row = str(date)+','+str(val)
     #            if count == 0:
     #                csv_writer.writerow( row )
     #            else:
     #                csv_writer.writerow( [ str(date) ] + [ str(val) ])
     #    print "File saved: %s " % ( search_query + '_google_report.csv' )


x = ArtData()
x.start()
# x.getArtnet("Banksy")
# x.makeartist()

