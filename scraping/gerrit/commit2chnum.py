#!/usr/bin/python3
#coding:utf8
from bs4 import BeautifulSoup
import requests
import pprint

u = 'http://gerrit.enflame.cn/q/+4a0f38d'
u = 'http://gerrit.enflame.cn/changes/7054d6dc6440453039848b1303b78c3c29962bb0'

def scrape_page_metadata(url):
    """Scrape target URL for metadata."""
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
    pp = pprint.PrettyPrinter(indent=4)
    r = requests.get(url, headers=headers)
    html = BeautifulSoup(r.content, 'html.parser')
    print(html)
    metadata = {
        # 'title': get_title(html),
        'description': get_description(html),
        # 'image': get_image(html),
        # 'favicon': get_favicon(html, url),
        # 'sitename': get_site_name(html, url),
        # 'color': get_theme_color(html),
        'url': url
        }
    pp.pprint(metadata)
    return metadata

def get_title(html):
    """Scrape page title."""
    title = None
    if html.title.string:
        title = html.title.string
    elif html.find("meta", property="og:title"):
        title = html.find("meta", property="og:title").get('content')
    elif html.find("meta", property="twitter:title"):
        title = html.find("meta", property="twitter:title").get('content')
    elif html.find("h1"):
        title = html.find("h1").string
    return title

def get_app(html):
    """Scrape page title."""
    title = None
    if html.title.string:
        title = html.title.string
    elif html.find("meta", property="og:title"):
        title = html.find("meta", property="og:title").get('content')
    elif html.find("meta", property="twitter:title"):
        title = html.find("meta", property="twitter:title").get('content')
    elif html.find("h1"):
        title = html.find("h1").string
    return title

def get_description(html):
    """Scrape page description."""
    description = None
    if html.find("meta", property="description"):
        description = html.find("meta", property="description").get('content')
    elif html.find("meta", property="og:description"):
        description = html.find("meta", property="og:description").get('content')
    elif html.find("meta", property="twitter:description"):
        description = html.find("meta", property="twitter:description").get('content')
    elif html.find("p"):
        description = html.find("p").contents
    return description


def get_image(html):
    """Scrape share image."""
    image = None
    if html.find("meta", property="image"):
        image = html.find("meta", property="image").get('content')
    elif html.find("meta", property="og:image"):
        image = html.find("meta", property="og:image").get('content')
    elif html.find("meta", property="twitter:image"):
        image = html.find("meta", property="twitter:image").get('content')
    elif html.find("img", src=True):
        image = html.find_all("img").get('src')
    return image

def mainf():
    data_list = []

    urls_new = [u]
    urls_old = []

    count = 1
    for url in urls_new:
        urls_old.append(url)
        print(urls_old)
        print ('Crawing %d url:%s' %(count, url))

        ##Download and Prettify Using BeautifulSoup
        response = urllib.urlopen(url)
        print(response.read())
        count = count + 1
        #print 'code:', response.getcode()
        if response.getcode() != 200 : #If crawing fails,start next url crawing
            print ('Crawing failed!')
            continue
        data = response.read()
        print(data)

    '''
        soup = BeautifulSoup(data)
        #print soup.prettify()
        #print soup #test crawing

        my_data = data_collect(url, soup)
        data_list.append(my_data)


    #    print('url:%s\ntitle:%s\nsummary:%s\n' %(data_want['url'], data_want['title'], data_want['summary']))

        ##Find urls and add them to urls_new
        links = soup.findAll('a', href = re.compile(r'/view/[0-9]*.htm'))
        for link in links:
            incomplete_url = link['href']
            complete_url = urlparse.urljoin(url, incomplete_url)
            if complete_url not in urls_new and complete_url not in urls_old:
                urls_new.append(complete_url)

    #    print('url:%s\ntitle:%s\nsummary:%s\n' %(data_want['url'], data_want['title'], data_want['summary']))

        if count > 5 : #Test 5 urls crawing
            break


    #print data_list #Test if data is correct
    print '\n------------------------------------------------------------------------'
    for dic in data_list:
        print('url:%s\ntitle:%s\nsummary:%s\n' %(dic['url'], dic['title'], dic['summary']))
    '''

if __name__ == '__main__':
    scrape_page_metadata(u)
    # mainf()