#!/usr/bin/env python

import sys,getopt,urllib2,json
from optparse import OptionParser

from PhEDExStuff import sites

  
# quick and dirty thing that just prints out where a dataset exists and % complete 

def main(argv):     

  if len(argv)<1:
    print "Usage: \n python %s dataset" % sys.argv[0]
    sys.exit(1)
  else:
    dataset=argv[0]

  print "For dataset: %s" % dataset

  sitelist=sites(dataset)

  for site in sitelist.keys():
    if sitelist[site]>1:
       print "Site: %25s   %.4f GB" % (site,sitelist[site] / 1000000000.0)
    else:
       print "Site: %25s  Complete %.1f " % (site,sitelist[site] * 100.0)
     
if __name__ == '__main__':
    main(sys.argv[1:])
  
