IP="http://10.155.15.81:8000/"

from pathlib import Path
from statistics import mean
from urllib.parse import urlparse, urljoin
import requests
from bs4 import BeautifulSoup
import time
import math
from sys import getsizeof

hun=[]
ten=[]
one=[]
tenmb=[]
totalSize=0
def averageOfList(num):
    sumOfNumbers = 0
    for t in num:
        sumOfNumbers = sumOfNumbers + t

    avg = sumOfNumbers / len(num)
    return avg
def sd_calc(data):
    n = len(data)

    if n <= 1:
        return 0.0

    mean, sd = averageOfList(data), 0.0

    # calculate stan. dev.
    for el in data:
        sd += (float(el) - mean)**2
    sd = math.sqrt(sd / float(n-1))

    return sd
def dinow(url,path):
    global totalSize
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception('status code is {} for {}'.format(r.status_code, url))
    content = r.text
    totalSize =totalSize+ getsizeof(content)
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
        
        for i in range(0,10000):
            s1=time.time()
            dinow(url,path)
            s2=time.time()
            hun.append(s2-s1)
       
        print("Mean 100B:- ")
        print(0.1/mean(hun))
        print("Std Dev 100B:- ")
        print(0.1/sd_calc(hun))
        print(f" - Total data transfered per file [bits] divided by file size [bits]: {(totalSize/int(10000)) / (0.1*1000)}")
        
    elif size=="10KB":
        
        for i in range(0,1000):
            s1=time.time()
            dinow(url,path)
            s2=time.time()
            ten.append(s2-s1)
       
        print("Mean 10kB:- ")
        print(10/mean(ten))
        print("Std Dev 10kB:- ")
        print(10/sd_calc(ten))
        print(f" - Total data transfered per file [bits] divided by file size [bits]: {(totalSize/int(1000)) / (10*1000)}")

 
    elif size=="1MB":
        
        for i in range(0,100):
            s1=time.time()
            dinow(url,path) 
            s2=time.time()
            one.append(s2-s1)
       
        print("Mean 1MB:- ")
        print(1000/mean(one))
        print("Std Dev 1MB:- ")
        print(1000/sd_calc(one))
        print(f" - Total data transfered per file [bits] divided by file size [bits]: {(totalSize/int(100)) / (1000*1000)}")

    elif size=="10MB":
        
        for i in range(0,10):
            s1=time.time()
            dinow(url,path)
            s2=time.time()
       
            tenmb.append(s2-s1)
       
        print("Mean 10MB:- ")
        print(10000/mean(tenmb))
        print("Std Dev 10MB:- ")
        print(10000/sd_calc(tenmb))
        print(f" - Total data transfered per file [bits] divided by file size [bits]: {(totalSize/int(10)) / (10000*1000)}")

    else:
        dinow(url,path)               

    


if __name__ == '__main__':
    downloadFiles(IP)
    
