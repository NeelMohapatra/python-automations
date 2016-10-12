#! /usr/bin/env python3
# Author: Swojit Mohapatra
# To open the spotify tab for me
# Q. Why did I do this?
# A. Because I am too lazy to open the browser and then click on spotify's bookmark #FWPs


import webbrowser, sys
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
webbrowser.get(chrome_path).open_new_tab('https://play.spotify.com/browse')
