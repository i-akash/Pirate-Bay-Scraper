#!../../scriptingEnv/bin/python


from util.pageDetails import PageDetails
from util.time import Time
import json
from pymongo import MongoClient

pageDetails=PageDetails()
with open('/home/akash/Documents/script/scraping/1.PirateBay/json/recenturls.json','r') as reader:
    url_list=json.load(reader)

alltorrents=[]
for url in url_list[1:100]:
    details=pageDetails.getDetail(url=url,recent=True)
    alltorrents.append(details)


client=MongoClient('mongodb://127.0.0.1:27017')
client.torrentapp.torrent.insert_many(alltorrents)
