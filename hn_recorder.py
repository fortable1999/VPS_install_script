#!/usr/bin/env python2
import sys
import pickle
from urllib2  import urlopen
from HTMLParser import HTMLParser as HTML_PARSER

HN_URL = 'https://news.ycombinator.com/'

def updated_callback(url, story):
    # print story, url
    pass

class HN_PARSER(HTML_PARSER):
    """
    Hacker News Parser Class
    """

    in_body = False
    in_title = False
    in_a = False
    news_url = ""
    result = {}

    def handle_starttag(self, tag, attrs):
        if tag == "body":
            self.in_body = True
            return
        if tag == "td" and "class" in dict(attrs) and dict(attrs)['class'] == "title":
            self.in_title = True
        if self.in_title and tag == "a":
            self.news_url = dict(attrs)['href']
            self.in_a = True

    def handle_endtag(self, tag):
        if self.in_title and tag == "a":
            self.in_a = False
        if tag == "td":
            self.in_title = False
        if tag == "body":
            self.in_body = False
            return

    def handle_data(self, data):
        if data == "More": return 
        if self.in_body and self.in_title and self.in_a:
            self.result[self.news_url] = data

def cached_loader():
    try:
        with open('data.pkl', 'rb') as f:
            return pickle.load(f)
    except IOError:
        return {}

def cache_saver(obj):
    with open('data.pkl', 'wb') as f:
        return pickle.dump(obj, f)

def updater():
    res = {}
    page = urlopen(HN_URL).read()
    parser = HN_PARSER()
    old_news = cached_loader()
    parser.feed(page)
    news = parser.result
    for k,v in news.items():
        if not k in old_news:
            res[k] = v
            updated_callback(k,v)
    if res:
        with open('index.html','w') as f:
            f.write("<html><body>%s</body></html>" % str(res))
    old_news = news
    cache_saver(news)

if __name__ == '__main__':
    updater()

