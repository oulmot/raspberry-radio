#!/usr/bin/env python
# Tom Luo
# tom.luo@cs.oxfordalumni.org
# Mar 20, 2015
# International Happiness Day

import subprocess as s
import sys

def usage():
        print 'Usage: radio.py BBC4'

def getURL(station):
        urls='/var/local/bbc_radio/urls'
        lines = open(urls).readlines()
        lines = [i.split(', ') for i in lines]
        a = [i[0] for i in lines]
        b = [i[1] for i in lines]
        d = dict(zip(a,b))
        try:
                return d[station]
        except KeyError:
                print 'Stations available:'
                print d.keys()
                return None

def main():
        try:
                station = sys.argv[1]
        except IndexError:
                usage()
                sys.exit()

        url = getURL(station.upper())

        if url:
                s.Popen(["mpc", "clear"])
                s.Popen(["mpc", "add", url.strip()])
                s.Popen(["mpc", "play"])


if __name__ == '__main__':
        main()