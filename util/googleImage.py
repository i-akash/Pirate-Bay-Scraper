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
        
        # <img id=key>
        # #imgrc=key
        # https://www.google.co.in/search?q=aladdin+hd+poster&source=lnms&tbm=isch#imgrc=key
        # img< class=irc_mut>


        # url="https://www.google.co.in/search?q={} {}&source=lnms&tbm=isch".format(query,"hd poster")
        # html=download(url)

        # if not html:
        #     return ""

        # tree=gettree(html)

        # id=getField(tree,'//img[@id]/@id')
        # print(id)
        # url=url+"#imgrc={}".format(id)
        # html=download(url)

        # if not html:
        #     return ""

        # tree=gettree(html)
        # poster=getField(tree,"//img[@class='irc_mut']/@src")
        # print(poster)

        # <img id=key>
        # #imgrc=key
        # https://www.google.co.in/search?q=aladdin+hd+poster&source=lnms&tbm=isch#imgrc=key
        # img< class=irc_mut>

        html=download('https://www.google.com/search?q={} {}&client=ubuntu&hs=oGr&channel=fs&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjXgdChgJnkAhVBHo8KHSH8AZoQ_AUIESgB&biw=1871&bih=949'.format(query,"hd poster"))
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


