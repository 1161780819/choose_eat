#coding:utf-8
import urllib2,os,urllib
from bs4 import BeautifulSoup

#解析每一页的目标url
def readurl(url):
    response = urllib2.urlopen(url)
    soup = BeautifulSoup(response,"html.parser")
    for i in soup.select('a[target]'):
        if "tkhf" in i.get('href'):
            dist_url = "http://www.99jbuc.com" + i.get("href")
            res = urllib2.urlopen(dist_url)
            so = BeautifulSoup(res,"html.parser")
            path = 'd:/myfile/' + i.get("href")
            if not os.path.exists(path):
                os.mkdir(path)
            mag = ""
            for m in so.select('img[data-original]'):
                imgurl = m.get('data-original')
                download_file(imgurl,path + "/")
            for n in so.select('div[class="n_bd"]'):
                for str in n.strings:
                    if "magnet" in str:
                        mag = str
                        fp = open(path + "/" + i.get("href") + ".txt",'w')
                        fp.write(mag)
                        fp.close()
                        print mag
            break

def download_file(url,dist_path):
    try:
        print os.path.basename(url)
        file = urllib2.urlopen(url)
        data = file.read()
        with open(dist_path + os.path.basename(url),"wb") as code:
            code.write(data)
    except:
        print "下载出错!重新请求"
        download_file(url,dist_path)

#爬虫入口
readurl(url = "http://www.99jbuc.com/palk_38.aspx")