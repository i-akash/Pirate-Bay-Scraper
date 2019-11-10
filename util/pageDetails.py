from util.yahooPoster import getPoster
from util.Util import download,gettree,arrayChecker
from util.time import Time
from util.dataCleaning import getClean,cleaner,titleCleaner
class PageDetails:
    def __init__(self):
        pass


    def torrentDetail(self,tree,recent=True):
        result={}
        details=arrayChecker(tree.xpath('//div[@id="detailsframe"]'),0)
        if details :  
            # top title  
            result['title']= titleCleaner(cleaner(arrayChecker(details.xpath('./div[@id="title"]/text()'),0)))
            result['poster']=getPoster(result['title'])

            # left col
            optionsTitle=details.xpath('./div[@id="details"]/dl[@class="col1"]/dt/text()')
            optionsData=details.xpath('./div[@id="details"]/dl[@class="col1"]/dd')

            i=0
            for title in optionsTitle :
                options=[]
                datas=optionsData[i].xpath('./a/text()')

                j=0
                for url in optionsData[i].xpath('./a/@href'):
                    options.append({"url": url,"text":cleaner(arrayChecker(datas,j))})
                    j=j+1

                for data in optionsData[i].xpath('./text()'):
                    options.append({"url":"","text":cleaner(data)})

                i=i+1
                
                result[title[:-1].lower().replace("(s)","").replace(" ","")]=options
            
            # right col
            optionsTitle=details.xpath('./div[@id="details"]/dl[@class="col2"]/dt/text()')
            optionsData=details.xpath('./div[@id="details"]/dl[@class="col2"]/dd')
            
            
            i=0
            for title in optionsTitle :
                options=[]
                datas=optionsData[i].xpath('./a/text()')

                j=0
                for url in optionsData[i].xpath('./a/@href'):
                    options.append({"url": url,"text":cleaner(arrayChecker(datas,j))})
                    j=j+1

                for data in optionsData[i].xpath('./text()'):
                    options.append({"url":"","text":cleaner(data)})

                i=i+1    
                result[title[:-1].lower().replace("(s)","").replace(" ","")]=options


            torrent_urls=details.xpath('./descendant::div[@class="download"]/a/@href')
            result['magnet_url']=torrent_urls[0]
            result['stream_url']=torrent_urls[1]
            result['screenshots']=getClean(details.xpath('./descendant::pre/a/@href'))
            result['overview']=getClean(details.xpath('./descendant::pre/text()'))
            result['recent']=recent
        return result


    def getDetail(self,url,recent=True):
        time=Time()
        html=download(url)
        time.print_time()
        
        if not html:
            return {}

        tree=gettree(html)
        
        if not tree:
            return {}

        details=self.torrentDetail(tree,recent)
        time.print_time()
        return details
