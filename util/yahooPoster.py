from util.Util import download,gettree,arrayChecker
from util.time import Time

def getField(tree,path=""):
        options=tree.xpath(path)
        option=arrayChecker(options,1)
        
        if not option:
            option=arrayChecker(options,0)
        return option
 

def getPoster(query="spider man"):
        time=Time()

        html=download('https://uk.images.search.yahoo.com/search/images;_ylt=AwrVpCHCYmFdst4A535NBQx.;_ylu=X3oDMTBsZ29xY3ZzBHNlYwNzZWFyY2gEc2xrA2J1dHRvbg--;_ylc=X1MDMjExNDcxNzAwNQRfcgMyBGFjdG4DY2xrBGNzcmNwdmlkA1RYSWNBVEV3TGpLWE5kUTBYVm1VNVFPd01qY3VNUUFBQUFBOU8ydVcEZnIDeWZwLXQtdWtmcGFmMDEyBGZyMgNzYS1ncARncHJpZAMEbl9zdWdnAzAEb3JpZ2luA3VrLmltYWdlcy5zZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDBHFzdHJsAzI3BHF1ZXJ5A2F2ZW5nZXJzJTIwZW5kZ2FtZSUyMHBvc3RlcgR0X3N0bXADMTU2NjY2MzM2Nw--?p={}+{}&fr=yfp-t-ukfpaf012&fr2=sb-top-uk.images.search&ei=UTF-8&n=60&x=wrt'.format(query,"poster"))
        time.print_time()
        
        if not html:
            return ""

        tree=gettree(html)
        if not tree:
            return ""

        poster=""
        poster=getField(tree,"//img/@src")
        time.print_time()
        return poster


