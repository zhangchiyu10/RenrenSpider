# -*- coding: utf-8 -*- 
import urllib2, urllib, cookielib,re,sys,time,MySQLdb
from bs4 import BeautifulSoup
while True:
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    urllib2.install_opener(opener)
    username="u_235@qq.com"
    pwd="th2010012028"
    domain = 'www.renren.com'#人人网的地址
    origURL = 'http://www.renren.com/Home.do'#人人网登录以后的地址
    data = {'domain':domain,'origURL':origURL,'email':username, 'password':pwd}
    print 'login.......'
    req = urllib2.Request('http://www.renren.com/PLogin.do',urllib.urlencode(data))
    page = opener.open(req)
    soup = BeautifulSoup(page.read())
    print soup.prettify()
    break
    #db=MySQLdb.connect(host='127.0.0.1',user='root',db='ghost_v1')
    #cur=db.cursor()
    #print 'database connnected'
    count=0
    total=0
    visited={"309531480":time.time()}#我
    initial="274036590"
    stack={initial:"".join(["http://www.renren.com/",initial,"/profile"])}#起始栈
    while len(stack)>0:
        t=time.strftime('%H:%M:%S',time.localtime(time.time()))
        id_now=stack.keys()[-1]#广度优先
        next=stack[id_now]
        try:
            r=urllib2.urlopen(next)
        except:
            total=total+1            
            print t,len(stack),id_now,count,"not exist"
        soup = BeautifulSoup(r.read())
        f=open("1.html","wb")
        f.write(str(soup.prettify().encode("utf-8")))
        f.close()
        visited[id_now]=time.time()
        exist=soup.find(attrs={"id":"visitors"})
        if exist==None:
            exist=soup.find(attrs={"id":"footprint-box"})
        if exist<>None:
            count=count+1
            #try:
            #    cur.execute('INSERT INTO visited values(%s,%s)',(id_now,int(0)))
            #except MySQLdb.IntegrityError:
            #    print "dup"                
            print t,len(stack),id_now,soup.html.head.title,count
            if len(stack)<50:#高枕无忧
                a=exist.findAll("a")
                for i in range(1,len(a)):
                    id=a[i]["namecard"]
                    if not visited.has_key(id) and not stack.has_key(id):
                        stack[id]="".join(["http://www.renren.com/",id])
        else:
            total=total+1
            print t,len(stack),id_now,count,"no rights"
        del stack[id_now]
        if count%100==0:
            del visited
            visited={"740267938":time.time()}
        elif count%20==0:
            db.commit()
    print ""
    break
