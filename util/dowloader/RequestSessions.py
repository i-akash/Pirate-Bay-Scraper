import requests

class RequestSessions:
    _instance=None
    
    @staticmethod
    def get_instance():
        if RequestSessions._instance==None:
            RequestSessions()
        return RequestSessions._instance


    def __init__(self):
        if RequestSessions._instance!=None:
            raise Exception("This class is a singleton!")
        else :
            RequestSessions._instance=self
            self.session=requests.Session()
    