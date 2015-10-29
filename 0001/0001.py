__author__ = 'chenyang'
import random
import string

s = 'abcdefghijklmnopqrstuvwlyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
for i in range(1,201):
  code =  string.join(random.sample(s,10)).replace(" ", "")
  print code