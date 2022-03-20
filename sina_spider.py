import requests, re

from lxml import etree

# 下载
url = 'http://blog.sina.com.cn/s/blog_593783dc0102ytta.html?tj=1'
resp = requests.get(url)
resp.encoding = 'utf8'
html = resp.text

# 解析
x_title = '//h2[@class="titName SG_txta"]/text()'
x_author = '//strong[@id="ownernick"]/text()'
x_content = '//div[@class="articalContent   newfont_family"]//p/text()'
x_dtime = '//span[@class="time SG_txtc"]/text()'

# 清洗
doc = etree.HTML(html)
title = doc.xpath(x_title)[0].strip()
author = doc.xpath(x_author)[0].strip()
origin_content = doc.xpath(x_content)
content = '\n'.join([c.strip() for c in origin_content if c.strip()])
dtime = doc.xpath(x_dtime)[0].strip()[1:-1]

# 阅读量
readn_url = 'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=593783dc0102ytta&ref=http%3A%2F%2Fblog.sina.com.cn%2F&varname=requestId_27563707'
readn_header = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'U_TRS1=000000fa.60387bca.5fb32191.1beb681f; UOR=,blog.sina.com.cn,; SINAGLOBAL=211.95.30.250_1605575057.870498; Apache=211.95.30.250_1605611395.951014; U_TRS2=000000fa.13597a60.5fb3af84.aac42187; ULV=1605611400535:3:3:3:211.95.30.250_1605611395.951014:1605611395621; rotatecount=3',
    'Host': 'comet.blog.sina.com.cn',
    'Referer': 'http://blog.sina.com.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
readn_resp = requests.get(readn_url, headers=readn_header)
readn_resp.encoding = 'utf8'
readn_html = readn_resp.text
rule = r'av":(\d+)'
readn = re.findall(rule, readn_html)[0]
print(title)
print(author)
print(content)
print(dtime)
with open('E-commerce.txt','w') as fp:
    fp.write(title)
    fp.write('\n')
    fp.write(f'作者：{author}'+'\n\n=================================================================================\n')
    fp.write(content+'\n\n\n')
    fp.write(f'阅读量:{readn}'+'    ')
    fp.write(dtime)
    fp.close()