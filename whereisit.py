#!/usr/bin/env python

import sys,getopt,urllib2,json
from optparse import OptionParser

from PhEDExStuff import sites

  
     

def main():     
  usage = "Usage $prog [options]"
  
  parser = OptionParser(usage=usage)
  
  parser.add_option("-d", "--dataset", action="store", type="string", default="/None/None/None", dest="dataset", help="return locations of dataset")
  
  (opts,args) = parser.parse_args()
  
  dataset=opts.dataset
  print "For dataset: %s" % dataset

  sitelist=sites(dataset)

  for site in sitelist.keys():
    print "Site: %25s  Complete %.1f " % (site,sitelist[site] * 100.0)
     
if __name__ == '__main__':
    main()
  