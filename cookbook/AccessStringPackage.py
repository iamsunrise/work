#/usr/bin/env python
#! coding = utf-8

import struct
def fields(baseformat,theline,lastfield=False):
    numremain = len(theline)-struct.calcsize(baseformat)
    format = "%s %d%s" % (baseformat,numremain,lastfield and "s" or "x")
    return struct.unpack(format,theline)
ret = fields("5s 3x 8s ss","this is a example access")
print ret
    
