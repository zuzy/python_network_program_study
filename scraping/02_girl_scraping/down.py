#!/usr/bin/python3
#coding: utf-8

# from requests import *
import requests 

def run():
    print("hello")
    resp = requests.get('http://www.baidu.com')
    print(resp.text)

# if __name__ == '__main__':
    # run()

def run_1():
    response = requests.get("http://www.newsimg.cn/big201710leaderreports/xibdj20171030.jpg") 
    with open("xijinping.jpg","wb") as f :
        f.write(response.content)   
        f.close


def run_2():
    # 头文件，header是字典类型
    headers = {
        "Host":"www.newsimg.cn",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5383.400 QQBrowser/10.0.1313.400"
    }
    response = requests.get("http://www.newsimg.cn/big201710leaderreports/xibdj20171030.jpg",headers=headers) 
    with open("xijinping_1.jpg","wb") as f :
        f.write(response.content)   
        f.close


if __name__ == "__main__":
    run()
    run_1()
    run_2()


