

#!/usr/bin/env python

import sys,getopt,urllib2,json
from optparse import OptionParser

from PhEDExStuff import blocksJSON

DiskJson=blocksJSON("T1_US_FNAL_Disk")
with open('T1_US_FNAL_Disk.json','w') as outfile:
  json.dump(DiskJson,outfile)
  
NewDiskJson=blocksJSON("T1_US_FNAL_New_Disk")
with open('T1_US_FNAL_New_Disk.json','w') as outfile:
  json.dump(NewDiskJson,outfile)