#! /usr/bin/env python3
# Author: Swojit Mohapatra
# To open new tabs of UW Course Catalogs. Just type in course codes as arguments
# Q. Why did I do this?
# A. Because it's redundant to google for 'XXX course catalogs' all the time


import webbrowser, sys
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
# Coz chrome isn't my default browser
if len(sys.argv) > 1:
    for course in map(str.lower, sys.argv[1:]):
        # Course codes need to be in lower case
        webbrowser.get(chrome_path) \
        .open_new_tab('https://www.washington.edu/students/crscat/' + course + \
        '.html')
else:
    print(r'''Pass in the course codes as arguments.
Something like ./uwCourse.py cse biol phys astr''')
