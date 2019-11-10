import requests
from util.dowloader.RequestSessions import RequestSessions

class Downloader:

    def __init__(self,url,user_agent='ws',proxies=None):
        self.base_url=url
        self.user_agent=user_agent
        self.proxies=proxies

        #Singleton session obejct 
        self.session=RequestSessions.get_instance().session

    def get(self,sub_url=''):
        print('Downloading : ',self.base_url+sub_url)

        try:
            resp=requests.get(self.base_url+sub_url,headers={'User-Agent':self.user_agent},proxies=self.proxies)
            html=resp.content
        except requests.RequestException as e:
            print("Download error :",e)
            html=None
        return html    
        