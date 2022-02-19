IP="http://10.153.5.9:8000/"

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
        pass
        # with open(path, 'w') as f:
            
        #     f.write(content)

def findLinks(content):
    soup = BeautifulSoup(content)
    
    for a in soup.findAll('a'):
       
        yield a.get('href')
def downloadFiles(url):
    global totalSize
    path = url.lstrip('/')
    size = urlparse(path).path.lstrip("/") +""

    file_name_to_size = {
    '100B': 100,
    '10KB': 10240,
    '1MB': 1048576,
    '10MB': 10320162,
    }   

    if size=="100B":
        totalSize = 0
        for i in range(0,10000):
            s1=time.time()
            dinow(url,path)
            s2=time.time()
            hun.append(file_name_to_size["100B"]/(s2-s1))
       
        print("Mean 100B:- ")
        print(mean(hun))
        print("Std Dev 100B:- ")
        print(sd_calc(hun))
        overhead = (totalSize/int(10000)) / file_name_to_size["100B"]
        print(f" - Total data transfered per file [bytes] divided by file size [bytes]: {(overhead)}")
        
    elif size=="10KB":
        totalSize = 0
        for i in range(0,1000):
            s1=time.time()
            dinow(url,path)
            s2=time.time()
            ten.append(file_name_to_size["10KB"]/(s2-s1))
       
        print("Mean 10kB:- ")
        print(mean(ten))
        print("Std Dev 10kB:- ")
        print(sd_calc(ten))
        overhead = (totalSize/int(1000)) / file_name_to_size["10KB"]
        print(f" - Total data transfered per file [bytes] divided by file size [bytes]: {(overhead)}")

 
    elif size=="1MB":
        totalSize = 0
        for i in range(0,100):
            s1=time.time()
            dinow(url,path) 
            s2=time.time()
            one.append(file_name_to_size["1MB"]/(s2-s1))
       
        print("Mean 1MB:- ")
        print(mean(one))
        print("Std Dev 1MB:- ")
        print(sd_calc(one))
        overhead = (totalSize/int(100)) / file_name_to_size["1MB"]
        print(f" - Total data transfered per file [bytes] divided by file size [bytes]: {(overhead)}")

    elif size=="10MB":
        totalSize = 0
        for i in range(0,10):
            s1=time.time()
            dinow(url,path)
            s2=time.time()
       
            tenmb.append(file_name_to_size["10MB"]/(s2-s1))
       
        print("Mean 10MB:- ")
        print(mean(tenmb))
        print("Std Dev 10MB:- ")
        print(sd_calc(tenmb))
        overhead = (totalSize/int(10)) / file_name_to_size["10MB"]
        print(f" - Total data transfered per file [bytes] divided by file size [bytes]: {(overhead)}")

    else:
        dinow(url,path)               

if __name__ == '__main__':
    downloadFiles(IP)
    
'''
Refrences:
https://www.tecmint.com/python-simplehttpserver-to-create-webserver-or-serve-files-instantly/
https://appdividend.com/2022/01/19/python-mean/
'''
