from util.pageUrls import PageUrls
from util.time import Time
import json

base_url='https://thepiratebay.org'
search_url='https://thepiratebay.org/search/*/{}/7//'

pageurls=PageUrls(base_url)


time=Time()
allurls=[]
for page in range(20):
    search_url=search_url.format(page)  
    urls=pageurls.getUrls(search_url)
    
    allurls=allurls+urls
    time.print_time()

with open('/home/akash/Documents/script/scraping/1.PirateBay/json/trendingurls.json','w') as writer:
    json.dump(allurls,writer,indent=4)
