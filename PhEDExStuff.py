#!/usr/bin/env python

import sys,getopt,urllib2,json,time

year=32000000 # a bit more but good enough
ayearago=int(time.time())-year*3


def sites(dataset):

  sitelist={}

  # pull block info down from datasvc
  dsQueryUrl='https://cmsweb.cern.ch/phedex/datasvc/json/prod/blockreplicas?dataset='

  fullQueryUrl=dsQueryUrl+dataset
  queryResult=urllib2.urlopen(fullQueryUrl).read()
  queryResult = queryResult.replace("\n", " ")
  queryJSON = json.loads(queryResult)
  
  # Now have dict full of stuff
  dssize=0.0
  for block in queryJSON['phedex']['block']:
    dssize+=block['bytes']
#    print block
    for replica in block['replica']:
      #print replica['node']
      if replica['node'] not in sitelist.keys():
         sitelist[replica['node']]=0
#      if replica['complete'] == 'y':
      sitelist[replica['node']] += replica['bytes']
         
  for site in sitelist.keys():
    sitelist[site]=sitelist[site]/dssize
  return sitelist
  
def blocksJSON(site):

  blocklist={}
  # get blocks living at a site
  stQueryUrl='https://cmsweb.cern.ch/phedex/datasvc/json/prod/blockreplicas?node='
  fullQueryUrl=stQueryUrl+site
  queryResult=urllib2.urlopen(fullQueryUrl).read()
  queryResult = queryResult.replace("\n", " ")
  queryJSON = json.loads(queryResult) 
  
  return queryJSON
  
def allSubscriptions(site):
  subslist={}
  # get all subscriptions since forever from a site
  stQueryUrl='https://cmsweb.cern.ch/phedex/datasvc/json/prod/subscriptions?node='+site+'&create_since=0'
  queryResult=urllib2.urlopen(stQueryUrl).read()
  queryResult = queryResult.replace("\n", " ")
  queryJSON = json.loads(queryResult) 
  
  return queryJSON
  
  
def allDeletionRequests(site):
  dellist={}
  # pull down all open deletion requests for a site
  stQueryUrl="https://cmsweb.cern.ch/phedex/datasvc/json/prod/deleterequests?node="+site+"&create_since="+str(ayearago)+"&approval=pending"
  queryResult=urllib2.urlopen(stQueryUrl).read()
  queryResult = queryResult.replace("\n", " ")
  queryJSON = json.loads(queryResult) 
  
  return queryJSON
  
  
if __name__ == '__main__':

   testsitelist=sites("/MinBias_TuneA2MB_13TeV-pythia8/Fall13-POSTLS162_V1-v1/GEN-SIM")
   for site in testsitelist.keys():
     print "Site: %25s  Complete %.1f " % (site,testsitelist[site] * 100.0)
     
   testJSON=blocksJSON("T3_US_FNALLPC")
   print testJSON
