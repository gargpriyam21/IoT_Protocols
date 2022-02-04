IP="http://192.168.86.20:8000/"

from pathlib import Path
from urllib.parse import urlparse, urljoin
import requests
from bs4 import BeautifulSoup
import time


def dinow(url,path):
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception('status code is {} for {}'.format(r.status_code, url))
    content = r.text
    if path.endswith('/'):
        
        Path(path.rstrip('/')).mkdir(parents=True, exist_ok=True)
        for link in findLinks(content):
            if not link.startswith('.'):
               
                downloadFiles(urljoin(url, link))
    else:
        with open(path, 'w') as f:
            
            f.write(content)

def findLinks(content):
    soup = BeautifulSoup(content)
    
    for a in soup.findAll('a'):
       
        yield a.get('href')
def downloadFiles(url):
    path = url.lstrip('/')
    size = urlparse(path).path.lstrip("/") +""
    if size=="100B":
        s1=time.time()
        for i in range(0,10000):
            dinow(url,path)
        s2=time.time()
        print("100B:- ")
        print(s2-s1)
    elif size=="10KB":
        s1=time.time()
        for i in range(0,1000):
            dinow(url,path)
        s2=time.time()
        print("10kB:- ")
        print(s2-s1)
    elif size=="1MB":
        s1=time.time()
        for i in range(0,100):
            dinow(url,path) 
        s2=time.time()
        print("1MB:- ")
        print(s2-s1)
    elif size=="10MB":
        s1=time.time()
        for i in range(0,10):
            dinow(url,path)
        s2=time.time()
        print("10MB:- ")
        print(s2-s1)
    else:
        dinow(url,path)               

    


if __name__ == '__main__':
    downloadFiles(IP)
    
