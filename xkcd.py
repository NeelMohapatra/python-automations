#! /usr/bin/env python3
import os, random
rand_num = random.randint(1, 1650)
print(rand_num)
link = os.popen("curl https://xkcd.com/" + str(rand_num) + "/  | grep 'Image URL'").read().split()[-1]

print(link)
img = link.split('/')[-1]
os.system('wget ' + link + ' && ./imgcat ' + img)
os.system('rm ' + img)
