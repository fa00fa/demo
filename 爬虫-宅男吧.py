import requests

from lxml import etree
from queue import Queue
from threading import Thread
from urllib.parse import urljoin, urlparse

BASE_URL = 'https://zhainanba.net/category/zhainanba/zhainantuku'

HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': '__51cke__=; Hm_lvt_835de570d623b13ece8c24875d30352b=1605621766; __tins__20921583=%7B%22sid%22%3A%201605621765458%2C%20%22vd%22%3A%2015%2C%20%22expires%22%3A%201605624074590%7D; __51laig__=15; Hm_lpvt_835de570d623b13ece8c24875d30352b=1605622275',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}


def download(url):
    '''下载 HTML 页面'''
    print(f'downloading: {url}')
    response = requests.get(url, headers=HEADERS)
    response.encoding = 'utf8'
    html = response.text.strip()
    return html

def clean_url(url):
    '''清洗 URL'''
    whole_url = urljoin(BASE_URL, url)
    if urlparse(whole_url).hostname == 'm.sohu.com':
        return whole_url
    else:
        return ''
    
def parse(html):
    new_urls = []
    article = {}
    doc = etree.HTML(html)
    if doc is None:
        return new_urls, article

    # 提取所有链接
    urls = doc.xpath('//a/@href')
    for url in urls:
        cleaned_url = clean_url(url)
        if cleaned_url:
            new_urls.append(cleaned_url)

    # 提取文章内容
    x_title = '//h2[@class="title-info"]/text()'
    x_author = '//header/span[@class="name"]/text()'
    x_dtime = '//footer/span[@class="time"]/text()'
    x_content = '//section[@id="articleContent"]//p/text()'

    try:
        # 进行数据清洗
        title = doc.xpath(x_title)[0].strip()
        author = doc.xpath(x_author)[0].strip()
        dtime = doc.xpath(x_dtime)[0].strip()
        content = doc.xpath(x_content)
    except IndexError:
        # 如果某个字段未取到值，直接放弃
        return new_urls, article

    # 将提取的字段存入 article
    article['title'] = title
    article['author'] = author
    article['dtime'] = dtime
    article['content'] = '\n'.join([line.strip() for line in content if line.strip()])
    return new_urls, article


def save(article):
    '''将文章存入文件'''
    if article:
        filename = f'{article["title"]}.txt'
        with open(filename, 'w') as fp:
            print(f'saving: {filename}')
            fp.write(article['title'])
            fp.write('\n')
            fp.write(article['author'])
            fp.write('\n')
            fp.write(article['dtime'])
            fp.write('===================================\n')
            fp.write(article['content'])


def spider(task_q, fetched_urls):
    '''单个爬虫线程的主任务'''
    while True:
        url = task_q.get()
        html = download(url)
        urls, article = parse(html)
        print(f'result: {urls}, {article}')

        # 保存文章
        save(article)

        # URL 去重
        new_urls = set(urls) - fetched_urls

        # 将新的 URL 放入队列
        for url in new_urls:
            task_q.put(url)

        # 将新的 URL 放入去重集合
        fetched_urls.update(new_urls)

        print(f'剩余任务: {task_q.qsize()}, 完成任务数: {len(fetched_urls)}')


def main(n_task):
    # 创建初始对象
    fetched_urls = set()
    fetched_urls.add(BASE_URL)  # 将首页放入去重集合

    task_q = Queue()
    task_q.put(BASE_URL)  # 将首页放入任务队列

    # 创建线程
    tasks = [Thread(target=spider, args=(task_q, fetched_urls)) for i in range(n_task)]
    for t in tasks:
        t.daemon = True
        t.start()

    for t in tasks:
        t.join()


if __name__ == "__main__":
    main(100)

