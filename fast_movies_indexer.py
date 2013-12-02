#!/usr/bin/env python

# Fast Movie Indexer Document
# this script generate a index.html for apache/nginx
# for example:
#
# $ ls
# helloworld.mp4
# 
# $ python fast_image_indexer.py
# $ ls index.html
# index.html
#
# Author: fortable1999@gmail.com

import sys
import os
import re

TEMPLATE = """
<html>
<title>Fast Movie Indexer</title>
<body>
<div align="center">
<h1>Fast Movie Indexer</h1>
<hr>
%s
</div>
<a href="https://github.com/fortable1999"><img style="position: absolute; top: 0; right: 0; border: 0;" src="https://s3.amazonaws.com/github/ribbons/forkme_right_red_aa0000.png" alt="Fork me on GitHub"></a>
</body>
</html>
"""
MOV_TEMPLATE = """
<h3>"{0}"</h3>
<br/>
<video width="80%" controls>
  <source src="{1}" type="video/mp4">
  Your browser does not support the video tag.
</video>
<hr>
"""

def render(movies):
    mov_html = ""
    for movie in movies:
        mov_html += MOV_TEMPLATE.format(movie, movie)
    return TEMPLATE % mov_html

def movie_finder():
    res = []
    for f in sorted(os.listdir('.')):
        if re.search(r'\.(mp4)$', f):
            res.append(f)
    return res

if __name__ == '__main__':
    with open("index.html", 'w') as html:
        html.write(render(movie_finder()))
