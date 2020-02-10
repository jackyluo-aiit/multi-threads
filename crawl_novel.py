import re
import requests
import os
from queue_demo import Queue
import threading
from datetime import datetime


def date_time_str(date_time):
    date_time_format = '%y-%M-%d %H:%M:%S'
    return datetime.strftime(date_time, date_time_format)


def query(url):
    print("...Loading webpage %s source code..." % url)
    return requests.get(url)


def extract_chapter_info(url):
    """
    extract the information of the novel and its chapters into a dictionary
    :param url:url of the target website
    :return: a list of hyper-links and names of each chapter
    """
    home_page = query(url)
    print("...Finished loading...")
    home_page_content = home_page.content
    home_page_str = home_page_content.decode('gbk')
    title = re.findall("title>(.*?)\(动物农场", home_page_str)
    print("title:", title)
    abstract = re.findall("<td class=\"p10-24\"><strong>内容简介：</strong><br />　　(.*?)</td", home_page_str)[0]
    print("abstract:", abstract)
    chapter_blocks = re.findall("strong>正文</strong></td>(.*?)</tbody", home_page_str, re.S)
    chapters = re.findall("href=\"(.*?)</a", chapter_blocks[0])
    print("There are %d chapters" % (len(chapters)))
    chapter_queue = Queue()
    for each in chapters:
        link, name = each.split("\">")
        link = url + "/" + link
        chapter_queue.put((name, link))
        print(name + ':' + link)
    return chapter_queue


def crawl_chapter_content(chapter_queue, threadID):
    """
    get every link of every chapter and crawl its content into a .txt file
    :param chapter_list: a dictionary contains chapters' name and their hyperlink
    :return:
    """
    while not chapter_queue.empty():
        qlock.acquire()
        try:
            chapter_name, chapter_link = chapter_queue.get(block=False)
            print(f"Thread {threadID} is processing {chapter_name}")
            qlock.release()
            chatper_content = query(chapter_link).content.decode('gbk')
            print(f"{chapter_name} length:{len(chatper_content)}")
            content = re.findall("p>(.*?)</p", chatper_content, re.S)
            article = content[0].replace("<br />", "\n")
            save(chapter_name, article)
        except Exception:
            qlock.release()


def save(chapter_name, article):
    os.makedirs('动物农场', exist_ok=True)
    with open(os.path.join('动物农场', chapter_name + '.txt'), 'w') as f:
        f.write(article)


if __name__ == '__main__':
    start = datetime.now()
    print(f"-----------Start from {date_time_str(start)}")
    base_url = "http://www.kanunu8.com/book3/6879"
    qlock = threading.Lock()
    workqueue = extract_chapter_info(base_url)
    t1 = threading.Thread(target=crawl_chapter_content, args=(workqueue, 1))
    t2 = threading.Thread(target=crawl_chapter_content, args=(workqueue, 2))
    t3 = threading.Thread(target=crawl_chapter_content, args=(workqueue, 3))
    t4 = threading.Thread(target=crawl_chapter_content, args=(workqueue, 4))
    multithread_start = datetime.now()
    print(f"-----------multi-threads start from {date_time_str(start)}")
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    end = datetime.now()
    print(f"------------End at {date_time_str(end)}")
    print(f"------------Multi-threads runtime: {end - multithread_start}")
    print(f"------------Total runtime: {end-start}")
