from util.dowloader.Downloader import Downloader
from util.Util import download,gettree,arrayChecker


class PageUrls:
    def __init__(self,base_url):
        self.base_url=base_url


    def getTorrentUrl(self,tree):
        result=[]
        torrent_urls=tree.xpath('//table[@id="searchResult"]/descendant::div[@class="detName"]/a/@href')
        
        for url in torrent_urls:
            result.append('{}{}'.format(self.base_url,url))
        return result

    def getUrls(self,url):
        html=download(url)
        if not html:
            return {}
        tree=gettree(html)
        if not tree:
            return {}
            
        torrent_urls=self.getTorrentUrl(tree)
        return torrent_urls
