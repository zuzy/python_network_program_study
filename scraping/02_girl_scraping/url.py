#!/usr/bin/python3
# coding: utf-8

import threading   #多线程模块
import re #正则表达式模块
import time #时间模块
import requests
import os

all_urls = []
all_img_urls = []
g_lock = threading.Lock()

pic_links = []

class Spider():
    def __init__(self, uri, header):
        self.uri = uri
        self.header = header
    def get_urls(self, start_page, end_page):
        self.all_urls = []
        global all_urls
        for i in range(start_page, end_page):
            url = self.uri % i
            all_urls.append(url)

class Producer(threading.Thread):
    def run(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
            'HOST':'www.meizitu.com'
        }
        global all_urls
        while len(all_urls) > 0:
            g_lock.acquire()
            pure_page = all_urls.pop()
            g_lock.release()
            try:
                print('analyse', pure_page)
                response = requests.get(url=pure_page, headers=headers, timeout=3)
                all_pic_link = re.findall('<a target=\'_blank\' href="(.*?)">',response.text,re.S)
                # print('all pic link', all_pic_link)
                global all_img_urls
                
                g_lock.acquire()
                all_img_urls += all_pic_link
                print(all_img_urls)
                g_lock.release()
                time.sleep(0.5)
            except Exception as e:
                pass

class _Consumer(threading.Thread):
    def run(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
            'HOST':'www.meizitu.com'
        }
        global all_img_urls
        print("%s is running" % threading.current_thread)
        while len(all_img_urls) > 0:
            g_lock.acquire()
            img_url = all_img_urls.pop()
            g_lock.release()
            try:
                response = requests.get(url=img_url, headers=headers)
                # response = requests.get(img_url, headers=headers, timeout=3)
                response.encoding = 'gb2312'
                title = re.search('<title>(.*?) | 妹子图</title>', response.text).group(1)
                all_pic_src = re.findall('<img alt=.*?src="(.*?)">', response.text, re.S)

                pic_dict = {title:all_pic_src}
                global pic_links
                g_lock.acquire()
                pic_links.append(pic_dict)
                print(title, '获取成功')
                g_lock.release()
            except Exception as e:
                print(e)
            time.sleep(0.2)

#消费者
class Consumer(threading.Thread) : 
    def run(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
            'HOST':'www.meizitu.com'
        }
        global all_img_urls   #调用全局的图片详情页面的数组
        print("%s is running " % threading.current_thread)
        while len(all_img_urls) >0 : 
            g_lock.acquire()
            img_url = all_img_urls.pop()
            g_lock.release()
            try:
                response = requests.get(img_url , headers = headers )
                response.encoding='gb2312'   #由于我们调用的页面编码是GB2312，所以需要设置一下编码
                title = re.search('<title>(.*?) | 妹子图</title>',response.text).group(1)
                all_pic_src = re.findall('<img alt=.*?src="(.*?)" /><br />',response.text,re.S)
                
                pic_dict = {title:all_pic_src}   #python字典
                global pic_links
                g_lock.acquire()
                pic_links.append(pic_dict)    #字典数组
                print(title+" 获取成功")
                g_lock.release()
                
            except:
                pass
            time.sleep(0.5)

class _DownPic(threading.Thread):
    def run(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
            'HOST':'www.meizitu.com'
        }
        while True:
            global pic_links
            g_lock.acquire()
            if len(pic_links) == 0:
                g_lock.release()
                continue
            else:
                pic = pic_links.pop()
                g_lock.release()
                for key, value in pic.items():
                    path=key.rstrip("\\")
                    is_exist = os.path.exists(path)
                    
                    if not is_exist:
                        os.makedirs(path)
                        print(path, '创建成功')
                    else:
                        print(path, '已经存在')
                    
                    for pic in value:
                        filename = path+'/'+pic.split('/')[-1]
                        if os.path.exists(filename):
                            continue
                        else:
                            try:
                                response = requests.get(pic, headers=headers)
                                with open(filename, 'wb') as f:
                                    f.write(response.content)
                                    f.close
                            except Exception as e:
                                print(e)


class DownPic(threading.Thread) :

    def run(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
            'HOST':'mm.chinasareview.com',
            'Cookie':'safedog-flow-item=; UM_distinctid=1634d30879a9-06230f37a83b4b8-38694646-1fa400-1634d30879c451; CNZZDATA30056528=cnzz_eid%3D1182386559-1526005899-http%253A%252F%252Fwww.meizitu.com%252F%26ntime%3D1526022264; bdshare_firstime=1526025336868'
        }
        while True:
            global pic_links
            # 上锁
            g_lock.acquire()
            if len(pic_links) == 0:
                # 不管什么情况，都要释放锁
                g_lock.release()
                continue
            else:
                pic = pic_links.pop()
                g_lock.release()
                # 遍历字典列表
                for key,values in  pic.items():
                    path=key.rstrip("\\")
                    is_exists=os.path.exists(path)
                    # 判断结果
                    if not is_exists:
                        # 如果不存在则创建目录
                        # 创建目录操作函数
                        os.makedirs(path) 
                
                        print (path+'目录创建成功')
                        
                    else:
                        # 如果目录存在则不创建，并提示目录已存在
                        print(path+' 目录已存在') 
                    for pic in values :
                        filename = path+"/"+pic.split('/')[-1]
                        if os.path.exists(filename):
                            continue
                        else:
                            try:
                                response = requests.get(pic,headers=headers, timeout=0.1)
                                with open(filename,'wb') as f :
                                    f.write(response.content)
                                    f.close
                            except Exception as e:
                                print(e)
                                pass



if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'HOST':'www.meizitu.com'
    }
    target_uri = 'http://www.meizitu.com/a/pure_%d.html'
    spider = Spider(target_uri, headers)
    spider.get_urls(1, 2)
    print(all_urls)

    threads = []
    for i in range(2):
        t = Producer()
        t.start()
        threads.append(t)
    

    for tt in threads:
        tt.join()

    # threads = []
    for i in range(10):
        t = _Consumer()
        t.start()
        threads.append(t)
    
    for i in range(10):
        t = _DownPic()
        t.start()
        threads.append(t)

    # for tt in threads:
    #     tt.join()

    print('运行到这里了!')

'''
这个网站已经不太能用了???不知道是不是被爬的...
'''