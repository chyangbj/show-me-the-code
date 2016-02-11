__author__ = 'chenyang'

import MySQLdb
import random
import string

connect =  MySQLdb.connect(host='mysql', user='root', passwd='123abc,.', db='flaskr')

s = 'abcdefghijklmnopqrstuvwlyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


for i in range(1,201):
  code =  string.join(random.sample(s,10)).replace(" ", "")
  cur = connect.cursor()
  cur.execute('insert into test0002 (code) values (%s)',code.encode('utf-8'))
  cur.close()

connect.commit()
