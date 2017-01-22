#! /usr/bin/env python3
import os, random
rand_num = random.randint(1, 1788)
os.system('curl -s https://xkcd.com/' + str(rand_num) + '/ > temp')
link = os.popen("grep 'Image URL' temp").read().split()[-1]

img = link.split('/')[-1]
os.system('wget -nv ' + link + ' && ./imgcat ' + img)
os.system('rm temp ' + img)
