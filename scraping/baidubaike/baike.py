#coding:utf8
#written by python 2.7
import re
import urllib
import urlparse
from BeautifulSoup import BeautifulSoup

def data_collect(url, soup):
    data_want = {}
    data_want['url'] = url
    title_node = soup.find('dd', attrs = {'class' : 'lemmaWgt-lemmaTitle-title'}).find('h1')
    data_want['title'] = title_node.getText()

    # <div class="lemma-summary" label-module="lemmaSummary">
    sum_node = soup.find('div', attrs = {'class' : 'lemma-summary'})
    data_want['summary'] = sum_node.getText()

    return data_want

data_list = list() #Store all the data of all urls crawed

urls_new = list() #Store urls that have not been crawed
urls_old = list() #Store urls that have been crawed

url = raw_input('Enter-')
if len(url) < 1 : url = 'http://baike.baidu.com/item/%E7%BA%A2%E5%8C%85/690774'

urls_new.append(url) # Add initial url to url_new

count = 1
while len(urls_new) > 0:
    url = urls_new.pop()
    urls_old.append(url)
    print ('Crawing %d url:%s' %(count, url))

    ##Download and Prettify Using BeautifulSoup
    response = urllib.urlopen(url)
    count = count + 1
    #print 'code:', response.getcode()
    if response.getcode() != 200 : #If crawing fails,start next url crawing
        print 'Crawing failed!'
        continue
    data = response.read()
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
