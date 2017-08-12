#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import sys, urllib
def reporthook(*a):print a
for url in sys.argv[:-1]:
    i = url.rfind('/')
    file = sys.argv[-1]+url[i+1:]
    print url,"->",file
    urllib.urlretrieve(url,file,reporthook)




