# -*- coding: gbk -*- 
import urllib2,re,time
from bs4 import BeautifulSoup
count=0
while True:
    req = urllib2.Request("http://3g.renren.com/profile.do?id=601648660&sid=jCYh06ao8gLYv0D0YTRL36&901emj&htf=2")
    response = urllib2.urlopen(req)
    soup = BeautifulSoup(response.read())
    #print soup.prettify()
    stack={}
    visited={"601648660":time.time()}#我是优灵
    for i in range(0,1):
        link="http://3g.renren.com/profile.do?entrytype=searchdo&htf=706&id=309531480&sid=jCYh06ao8gLYv0D0YTRL36&zy5bgu&from="
        id=link[35:44]
        stack[id]=link
    while len(stack)>0:
        id_now=stack.keys()[-1]
        next=stack[id_now]
        r=urllib2.urlopen(next)
        soup = BeautifulSoup(r.read())
        visited[id_now]=time.time()
        exist=soup.find(attrs={"class":"ssec"})
        if exist<>None:
            count=count+1
            print len(stack),id_now,count#,exist.p.b.contents[0]
            a=exist.contents[2].findAll("a")
            if len(a)>2:
                for i in range(1,len(a)-1):
                    link=a[i]["href"]
                    id=link[35:44]
                    if not visited.has_key(id) and not stack.has_key(id):
                        stack[id]=link
        else:
            shy=soup.find(attrs={"class":"notice_y"})
            if shy <>None:
                print len(stack),id_now,count,"加为好友才可查看更多信息"
            else:
                print stack[id_now]
        del stack[id_now]
        time.sleep(2)
    del visited
    del stack

    

            






