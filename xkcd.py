#! /usr/bin/env python3
# To display random comics from xkcd in iTerm2 and obviously you need iTerm2 for this
import os
os.system('curl -sL c.xkcd.com/random/comic/ > temp')
link = os.popen("grep 'Image URL' temp").read().split()[-1]

img = link.split('/')[-1]
os.system('wget -q ' + link + ' && ./imgcat ' + img)
os.system('rm temp ' + img)
