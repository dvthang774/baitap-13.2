import os
tm = input('Ten thu muc: ')
tt = input('Ten tep tin: ')
n = input('noi luu tru: ')
os.chdir(n)
os.mkdir(tm)
x = n + tm
os.chdir(x)
f = open(tt, "w")
f.writesline('hello world')
f.close()
