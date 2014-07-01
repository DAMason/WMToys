#!/usr/bin/env python

import sys,getopt,urllib2,json


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
    #print block['name']
    for replica in block['replica']:
      #print replica['node']
      if replica['node'] not in sitelist.keys():
         sitelist[replica['node']]=0
      if replica['complete'] == 'y':
         sitelist[replica['node']] += replica['bytes']
         
  for site in sitelist.keys():
    sitelist[site]=sitelist[site]/dssize
  return sitelist
  
if __name__ == '__main__':

   testsitelist=sites("/MinBias_TuneA2MB_13TeV-pythia8/Fall13-POSTLS162_V1-v1/GEN-SIM")
   for site in testsitelist.keys():
     print "Site: %25s  Complete %.1f " % (site,testsitelist[site] * 100.0)
   
