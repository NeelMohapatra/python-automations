#! /usr/bin/env python3
# Author: Swojit Mohapatra
# To open new tabs of UWCSE websites. Just type in course numbers as arguments
# Q. Why did I do this?
# A. Because I want to make the world a better place by solving one FWP at a time


import webbrowser, sys
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

if len(sys.argv) > 1:
    for num in sys.argv[1:]:
        if len(num) > 3:
            webbrowser.get(chrome_path).open_new_tab('https://courses.cs.washington.edu/courses/' + num[0:3] + '/' + num[3:])
        else:
            webbrowser.get(chrome_path).open_new_tab('https://cs.uw.edu/' + num)
else:
    print('\tPass in the course numbers [or quarter numbers] as arguments.')
