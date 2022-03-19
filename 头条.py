BASE_URL = 'https://m.sohu.com/'
HEADERS = {
    'Accept': '*/*',
    'Accept-Encoding': 'Gzip, deflate, br',
    'Accept-Language': 'Zh-CN,zh;q=0.9',
    'Sec-Fetch-Fest': 'Image',
    'Sec-Fetch-Mode': 'No-cors',
    'Sec-Fetch-Site': 'Cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

from lxml import etree
import requests
from queue import Queue
from threading import Thread
from urllib.parse import urljoin, urlparse


def download(url):
    resp = requests.get(url, headers=HEADERS)
    resp.encoding = 'utf8'
    html = resp.text
    return html


def clean_url(url):
    whole_url = urljoin(BASE_URL, url)
    if urlparse(whole_url).hostname == 'm.sohu.com':
        return whole_url
    else:
        return ''


def parse(html):
    new_urls = []
    article = {}
    doc = etree.HTML(html)
    '''提取url'''
    if doc is None:
        return new_urls, article
    urls = doc.xpath('//a/@href')
    for url in urls:
        cleaned_url = clean_url(url)
        if cleaned_url:
            new_urls.append(cleaned_url)

    '''提取文章内容'''
    x_title = '//h2[@class="title-info"]/text()'
    x_author = '//span[@class="name"]/text()'
    x_dtime = '//span[@class="time"]/text()'
    x_content = '//section[@class="article-content"]//p/text()'

    try:
        title = doc.xpath(x_title)[0].strip()
        author = doc.xpath(x_author)[0].strip()
        dtime = authot = doc.xpath(x_dtime)[0].strip()
        org_content = doc.xpath(x_content)
        content = '\n'.join([c.strip() for c in org_content if c.strip()])
    except IndexError:
        return new_urls, article
    else:
        article['title'] = title
        article['author'] = author
        article['content'] = content
        article['dtime'] = dtime
        return new_urls, article


def save(article):
    if article:
        filename = f'./今日头条/{article["title"]}.txt'
        with open(filename, 'w') as fp:
            fp.write(article['title'] + '\n')
            fp.write(article['author'] + '\n')
            fp.write(
                '==============================================================================================' + '\n')
            fp.write(article['content'] + '\n')
            fp.write(article['dtime'] + '\n')


def spider(featch_url, task_q):
    while True:
        url = task_q.get()
        html = download(url)
        new_urls, article = parse(html)
        save(article)

        required_url = set(new_urls) - featch_url
        for url in required_url:
            task_q.put(url)
        featch_url.update(required_url)

def main(n_task):
    featch_url = set()
    featch_url.add(BASE_URL)

    task_q = Queue()
    task_q.put(BASE_URL)

    tasks = [Thread(target=spider, args=(featch_url, task_q)) for i in range(n_task)]
    for t in tasks:
        t.daemon = True
        t.start()
    for t in tasks:
        t.join()


if __name__ == '__main__':
    main(100)
