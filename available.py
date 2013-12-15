# -*- coding: utf-8 -*- 
import urllib2, urllib, cookielib,re,sys,time,MySQLdb
from bs4 import BeautifulSoup
t1=time.time()
while True:
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    urllib2.install_opener(opener)
    username="ghost_v2@qq.com"
    pwd="th2010012028"
    domain = 'www.renren.com'#人人网的地址
    origURL = 'http://www.renren.com/Home.do'#人人网登录以后的地址
    data = {'domain':domain,'origURL':origURL,'email':username, 'password':pwd}
    print 'login renren.......'
    req = urllib2.Request('http://www.renren.com/PLogin.do',urllib.urlencode(data))
    page = opener.open(req)
    soup = BeautifulSoup(page.read())
    #print soup.prettify()
    db=MySQLdb.connect(host='127.0.0.1',user='root',db='rrr')
    cur=db.cursor()
    print 'database connnected'
    
    l=cur.execute("SELECT * FROM visited")
    for id in cur.fetchall():
        next="".join(["http://www.renren.com/",id[0]])
        #t=time.strftime('%H:%M:%S',time.localtime(time.time()))
        try:
            r=urllib2.urlopen(next)
        except:
            print t,len(stack),id_now,count,"not exist"
        print id[0]
        soup = BeautifulSoup(r.read())
        print soup.html.head.title
    t2=time.time()
    print (t2-t1)
    input()
    break
