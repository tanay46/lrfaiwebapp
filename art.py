import urllib
import re
from pyGTrends import pyGTrends
import csv, datetime, time, getpass, sys
import json
import os
import datetime
import pymongo
from pymongo import MongoClient

class ArtData:

  def __init__(self, name):
    self.artistname = name
    self.MONGOHQ_URL= "mongodb://tanay:tanay@oceanic.mongohq.com:10049/artists"

  def makeartist(self):
    wiki = self.wikipedia()
    instagram = self.instagram()
    googletrends = self.googletrends()
    artist = {"name": self.artistname,
              "wiki" : wiki,
              "instagram" : instagram,
              "google" : googletrends
              }
    client = MongoClient(self.MONGOHQ_URL)
    db = client.artists
    collection = db.artists
    artist_id = collection.insert(artist)
    print artist_id


  def wikipedia(self):
    # Get a file-like object for the Python Web site's home page.
    values = []
    months = []
    wiki = {}
    for i in range(1,13):
      if i < 10:
        yearmonth = "20130" + str(i)
      else:
        yearmonth = "2013" + str(i)
      website = "http://stats.grok.se/en/" + yearmonth + "/" + self.artistname 
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
      website = "http://stats.grok.se/en/" + yearmonth + "/" + self.artistname 
      f = urllib.urlopen(website)
      s = f.read()
      regex = re.compile("has been viewed (\d*)")
      r = regex.search(s)
      wiki[yearmonth] = int(r.groups()[0])
      values.append(int(r.groups()[0]))
      months.append(yearmonth)
      f.close()
    print "finished wiki"
    return wiki
    # print values
    # print months

  def googletrends(self):
    return self.getGTData(self.artistname)

  def instagram(self):
    clientid = "d88fc4bf02b84531b4b908d806d1c101" 
    namenospace = self.artistname.replace(' ', '')
    url = "https://api.instagram.com/v1/tags/"+ namenospace + "?client_id=" + clientid
    f = urllib.urlopen(url)
    s = f.read()
    x = json.loads(s)
    if x['meta']['code'] == 200:
      number = x['data']['media_count']
      print "finished insta"
      return number

  def getGTData(self, search_query = "debt", date="all", geo="all", scale="1", position = "end" ):
    print search_query
    dict = {}
    endlist = []
    countlist = []
    connector = pyGTrends( "larotondeapi", "dstegroup1")
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
      if " " and "-" in date:
        enddate = date.split(" ")[2]
        if (len(item[1])>0):
          try:
            count = int(item[1])
            dict[enddate] = count
            endlist.append(enddate[5:])
            countlist.append(count)
          except:
            break
    print dict
    return dict


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


x = ArtData("Andy Warhol")
x.makeartist()

