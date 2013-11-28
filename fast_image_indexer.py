#!/usr/bin/env python

# Fast Image Indexer Document
# this script generate a index.html for apache/nginx
# for example:
#
# $ ls
# image1.png image2.jpg
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
<title>Fast Image Indexer</title>
<body>
<div align="center">
%s
</div>
</body>
</html>
"""
IMG_TEMPLATE = """
<img src="%s" align="middle"></img>
"""

def render(images):
	img_html = ""
	for img in images:
		img_html += IMG_TEMPLATE % img
	
	return TEMPLATE % img_html

def image_finder():
	res = []
	for f in sorted(os.listdir('.')):
		if re.search(r'\.(bmp|jpg|png|jpeg)$', f):
			print type(f)
			res.append(f)
	return res

if __name__ == '__main__':
	with open("index.html", 'w') as html:
		html.write(render(image_finder()))
