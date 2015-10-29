__author__ = 'chenyang'
# write into a file

import random
import string

s = 'abcdefghijklmnopqrstuvwlyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
f = open('code.txt', 'w')

for i in range(1,201):
  code =  string.join(random.sample(s,10)).replace(" ", "")
  f.write(code)
  f.write('\n')
f.close()
