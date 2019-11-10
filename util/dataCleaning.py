

import re

def cleaner(data):
    data=re.sub('\n+',"",data)
    data=re.sub('\r+',"",data)
    data=re.sub('^ +',"",data)
    data=re.sub('\u00a0+',"",data)
    return data    

def titleCleaner(title):
    title=re.sub(r"\."," ",title)
    title=re.sub(r"\("," ",title)
    title=re.sub(r"\)"," ",title)
    title=re.sub(r"\["," ",title)
    title=re.sub(r"\]"," ",title)

    year=re.search("20[\d]*",title) 
    if year==None:
        year=re.search("19[\d]*",title)
    
    title=re.sub("20.*","",title)
    title=re.sub("19.*","",title)
    if year :
        title='{} {}'.format(title,year[0])

    return title


def getClean(datas):
    result=[]
    for data in datas:
        data=cleaner(data)
        if len(data)>0:
            result.append(data)

    return result


