#!/usr/bin/env python
# udpate_bbc_urls.py
# Tom Luo
# Mar 20, 2015

import urllib2, re

playlist="/var/local/bbc_radio/urls"
radios={}

radios["BBC1"]="http://www.radiofeeds.co.uk/bbcradio1.pls"
radios["BBC1x"]="http://www.radiofeeds.co.uk/bbc1xtra.pls"
radios["BBC2"]="http://www.radiofeeds.co.uk/bbcradio2.pls"
radios["BBC3"]="http://www.radiofeeds.co.uk/bbcradio3.pls"
radios["BBC4"]="http://www.radiofeeds.co.uk/bbcradio4fm.pls"
radios["BBC4x"]="http://www.radiofeeds.co.uk/bbcradio4extra.pls"
radios["BBC5l"]="http://www.radiofeeds.co.uk/bbc5live.pls"
radios["BBC5lx"]="http://www.radiofeeds.co.uk/bbc5livesportsextra.pls"
radios["BBC6"]="http://www.radiofeeds.co.uk/bbc6music.pls"


open(playlist,'w').close()
f = open(playlist,'a')

for station in radios:
   pls = radios[station]
   url = urllib2.urlopen(pls).read().split()[1]
   url = re.search("(?P<url>https?://[^\s]+)", url).group("url")
   print station,',',url
   f.write(station+','+url.strip()+'\n')

f.close()
