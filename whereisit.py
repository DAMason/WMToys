#!/usr/bin/env python

import sys,getopt,urllib2,json
from optparse import OptionParser

dsQueryUrl='https://cmsweb.cern.ch/phedex/datasvc/json/prod/blockreplicas?dataset='

def sites(dataset):

  sitelist={}

  # pull block info down from datasvc
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
  
     

def main():     

  usage = "Usage $prog [options]"
  
  parser = OptionParser(usage=usage)
  
  parser.add_option("-p", "--propose", action="store_true", default=False, dest="propose", help="return proposed site and exit")
  
  (opts,args) = parser.parse_args()

  sitelist=sites("/DarkMatter_Monojet_M-400_AV_Tune4C_13TeV-madgraph/Spring14dr-PU_S14_POSTLS170_V6-v1/AODSIM")
  
  for site in sitelist.keys():
    print "Site: %s  Complete %f " % (site,sitelist[site] * 100.0)
     
if __name__ == '__main__':
    main()
  