from util.pageUrls import PageUrls
from util.time import Time
import json

base_url='https://thepiratebay.org'
pageurls=PageUrls(base_url)
time=Time()
allurls=[]
for page in range(20):
    extension='/recent'
    if page:
        extension=extension+'/'+str(page)  
    urls=pageurls.getUrls(base_url+extension)
    allurls=allurls+urls
    time.print_time()

with open('/home/akash/Documents/script/scraping/1.PirateBay/json/recenturls.json','w') as writer:
    json.dump(allurls,writer,indent=4)
