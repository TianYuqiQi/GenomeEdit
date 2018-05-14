import urllib
import urllib.request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import time
from selenium import webdriver
file=open('C:\\Users\\KK\\Desktop\\fabG\\allfabG.txt','w')
url='https://www.ncbi.nlm.nih.gov/gene/?term=fabG'
geneurl='https://www.ncbi.nlm.nih.gov/'
data=[]
html=urllib.request.urlopen(url)
bsObj=BeautifulSoup(html)
geneurllist=[]
for i in bsObj.find('tbody').findAll('tr'):
    geneurllist.append(geneurl+i.find('a')['href'])
for i in geneurllist:
    html1=urllib.request.urlopen(i)
    bsObj1=BeautifulSoup(html1)
    print(bsObj1.findAll('h1')[1].get_text().replace('[','').replace(']','').strip())
    temp=bsObj1.findAll('a')
    fastaurl=''
    for i in temp:
        if i.get_text()=='FASTA':
            if 'report' in i['href']:
                fastaurl=i['href']
                break
    driver=webdriver.PhantomJS(executable_path='C:\\Users\\KK\\Desktop\\phantomjs-2.1.1-windows\\bin\\phantomjs')
    driver.get(geneurl+fastaurl)
    time.sleep(3)
    data.append(driver.find_element_by_id('viewercontent1').text)
    driver.close()
for i in data:
    file.write(i+"\n")
file.close()
