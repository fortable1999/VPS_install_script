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
{0}
</div>
<a href="https://github.com/fortable1999"><img style="position: absolute; top: 0; right: 0; border: 0;" src="https://s3.amazonaws.com/github/ribbons/forkme_right_red_aa0000.png" alt="Fork me on GitHub"></a>
</body>
</html>
"""
IMG_TEMPLATE = """
<img src="{0}" align="middle"></img>
"""

def render(images):
	img_html = ""
	for img in images:
		img_html += IMG_TEMPLATE.format(img)
	
	return TEMPLATE.format(img_html)

def image_finder():
	res = []
	for f in sorted(os.listdir('.')):
		if re.search(r'\.(bmp|jpg|png|jpeg)$', f):
			res.append(f)
	return res

if __name__ == '__main__':
	with open("index.html", 'w') as html:
		html.write(render(image_finder()))
