#! /usr/bin/env python3
import os, random
os.system('curl -sL c.xkcd.com/random/comic/ > temp')
link = os.popen("grep 'Image URL' temp").read().split()[-1]

img = link.split('/')[-1]
os.system('wget -q ' + link + ' && ./imgcat ' + img)
os.system('rm temp ' + img)
