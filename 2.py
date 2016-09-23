#coding=utf-8
import MySQLdb
import sys,time
from progressbar import *
import os

os.system("cls")
conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='123qwe',
        db ='123'
        )
cur=conn.cursor()
widgets = ['Progress: ', Percentage(), ' ', Bar(marker=RotatingMarker('>-=')),
           ' ', ETA(), ' ', FileTransferSpeed()]
pbar = ProgressBar(widgets=widgets, maxval=117205873).start()
for i in range(117205873):
    try:
        conn.ping()
    except:
        conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='123qwe',
        db ='123',
        cursorclass = MySQLdb.cursors.DictCursor
        )
    sql="select id from ids where flag = 1 limit "+bytes(i)+",1;"
    cur.execute(sql)
    data = cur.fetchone()
    #print "first: %s " % data
    
    sql1= "select password from ids where id = %s"
    cur.execute(sql1,data)
    pw = cur.fetchone()
    #print "second: %s " % pw
    
    sql2="update idemail set password = \""+str(pw[0])+"\" where mail = \""+str(data[0])+"\";"
    #print sql2
    cur.execute(sql2)
    
    sql3="update ids set flag = 0 where id = %s;"
    cur.execute(sql3,data)
    
    pbar.update(i+1)

cur.close()
conn.commit()
conn.close()