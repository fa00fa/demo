# coding:utf-8
import urllib2


def download1(url):
    reponse = urllib2.urlopen(url, timeout=5)
    print type(reponse)
    print reponse.info()
    print reponse.read(100)


url="http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=java&p=1&isadv=0" #urlopen只能处理http.不可以处理https

download1(url)
