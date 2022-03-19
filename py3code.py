# encoding:utf-8
import urllib.request
# urllib.request == urllib2

def download1(url):
    reponses = urllib.request.urlopen(url)
    while True:
        line = reponses.readline()
        print (line)
        if not line:
            break


url = 'http://www.baidu.com'

download1(url)
