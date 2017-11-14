
#!/usr/bin/env python

import sys,getopt,urllib2,json

def main(argv): 
    jj={}
  
    if (len(argv)<1):
      print "Usage" 
      print " python %s file" % sys.argv[0]
      sys.exit(1)
    else:
      infile=argv[0]
      
    with open(infile,'r') as jsoninput:
      jj=json.load(jsoninput)
      jsoninput.close()
      
    for block in jj['phedex']['block']:
      #print block
      print "%s %i %i %d %s" % (block['name'],block['bytes'],block['files'],block['replica'][0]['time_update'],block['replica'][0]['group']) 
      
      
if __name__ == '__main__':
    main(sys.argv[1:])