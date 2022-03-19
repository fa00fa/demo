import requests
from lxml import etree
from queue import Queue
from threading import Thread
from urllib.parse import urljoin, urlparse

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


# 下载
def download(url):
    print(f'正在下载{url}页面')
    resp = requests.get(url, headers=HEADERS)
    resp.encoding = 'utf8'
    html = resp.text.strip()
    return html


def clean_url(url):
    whole_url = urljoin(BASE_URL, url)
    if urlparse(whole_url).hostname == 'm.sohu.com':
        return whole_url
    else:
        return ''


def parse(html):
    '''提取url'''
    new_urls = []
    article = {}
    doc = etree.HTML(html)
    if doc is None:
        return new_urls, article

    '''提取所有链接'''
    x_url = '//a/@href'
    urls = doc.xpath(x_url)
    '''将缺少域名的的链接补充完整'''
    for url in urls:
        cleaned_url = clean_url(url)
        if cleaned_url:
            new_urls.append(cleaned_url)

    '''提取文章内容'''
    x_title = '//h2[@class="title-info"]/text()'
    x_author = '//span[@class="name"]/text()'
    x_dtime = '//span[@class="time"]/text()'
    x_content = '//section[@class="article-content"]//p/text()'
    '''解析后可能某些字段为空，取第0个会报错，因此如果缺少某个字段的东西就丢弃'''
    try:
        title = doc.xpath(x_title)[0].strip()
        author = doc.xpath(x_author)[0].strip()
        dtime = doc.xpath(x_dtime)[0].strip()
        ori_content = doc.xpath(x_content)
        content = '\n'.join([c.strip() for c in ori_content if c.strip()])
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
        filename = f"./搜狐新闻/{article['title']}.txt"
        print(f'正在保存{filename}')
        with open(filename, 'w') as fp:
            fp.write(article['title'])
            fp.write('\n')
            fp.write(article['author'])
            fp.write('\n')
            fp.write('======================================================================')
            fp.write(article['content'])
            fp.write('\n')
            fp.write('----------------------------------------------------------------------')
            fp.write(article['dtime'])
            print(article['content'])



def spider(task_q, fetched_urls):
    '''单个爬虫线程的任务'''
    while True:
        url = task_q.get()
        html = download(url)
        urls, article = parse(html)
        save(article)
        '''去重后的url放到队列里面'''
        new_urls = set(urls) - fetched_urls
        for url in new_urls:
            task_q.put(url)

        '''将去重后的url再放到全局的去重集合里'''
        fetched_urls.update(url)
        print(f'剩余任务书{task_q.qsize()},已完成{len(fetched_urls)}')


def main(n_task):
    # 创建初始对象
    fetched_urls = set()
    fetched_urls.add(BASE_URL)  # 将首页放到去重集合

    task_q = Queue()
    task_q.put(BASE_URL)  # 将首页放到队列里

    # '''创建线程'''
    tasks = [Thread(target=spider, args=(task_q, fetched_urls)) for i in range(n_task)]
    for t in tasks:
        t.daemon = True
        t.start()

    for t in tasks:
        t.join()


if __name__ == '__main__':
    main(100)
