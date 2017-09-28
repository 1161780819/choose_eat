#coding:utf-8
#多线程的应用及理解

import threading
from time import ctime,sleep

def music():
    for i in range(2):
        print "I was listening to music.===%s" %ctime()
        sleep(1)

def movie():
    for i in range(2):
        print "I was looking at movies.===%s" %ctime()
        sleep(5)

thd = []
t1 = threading.Thread(target=music)
t2 = threading.Thread(target=movie)
thd.append(t1)
thd.append(t2)

if __name__ == '__main__':
    for t in thd:
        t.setDaemon(True)
        t.start()
    t.join()
    print "over %s" %ctime()