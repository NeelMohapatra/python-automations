#! /usr/bin/env python3
# To display random comics from xkcd in iTerm2 and obviously you need iTerm2 for this

import os, json, argparse, requests

page = json.loads(requests.get('http://xkcd.com/info.0.json').text)
link = page['img']
img = link.split('/')[-1]
os.system('wget -q ' + link + ' && ./imgcat ' + img)
