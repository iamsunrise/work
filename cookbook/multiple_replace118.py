 #!/usr/bin/env python
 # coding:utf-8
import re
def multiple_replace(text,adict):
    rx = re.compile('|'.join(map(re.escape,adict)))
    def one_xlat(match):
        return adict[match.group(0)]
    return rx.sub(one_xlat,text)

def make_xlat(*args,**kwds):
    adict = dict(*args,**kwds)
    rx = re.compile('|'.join(map(re.escape,adict)))
    def one_xlat(match):
        return adict[match.group(0)]
    def xlat(text):
        return rx.sub(one.xlat,text)
    return xlat


