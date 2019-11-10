from util.dowloader.Downloader import Downloader
from lxml.html import fromstring


def download(url,extension=''):
    d=Downloader(url+extension)
    html=d.get()
    return html

def gettree(html):
    try:
        tree=fromstring(html)
    except Exception as e:
        tree=None
    return tree

def arrayChecker(a,index):
    if len(a)>index:
        return a[index]
    else :
        return None    
