#!/usr/bin/env python

import os
ipaddrfile = []
ipAddrTxt = 'ipAddr.txt'
ipAddrFile = file(ipAddrTxt)
ipAddrline = ipAddrFile.readlines()
for lines in ipAddrline:
	line = lines.strip("\n")
	line = lines.strip()
	ipaddrfile.append(line)
ipAddrFile.close()
print ipaddrfile
#count hall number
hallNumCount = 0
for lines in ipaddrfile:
	print lines
	if str(hallNumCount+1) == lines:
		 hallNumCount = hallNumCount+1
print hallNumCount

#conver ipAddrFile to dict
#chriet = {(ip: ),(port: ),(model:)}
def lookupIP(data,hallNum,machineMode):
	return data[hallNum].get[machineMode]
seq = ()
ipFile = {}
def initFile(data):
	labels = ("ip","port","model")
	for i in range(1,hallNumCount):
		print i
		data[i][chriet] = {}
		data[i][doremi] = {}
		data[i][dolby] = {}
                
initFile(ipFile)
print ipFile 
