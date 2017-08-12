#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import shlex
import subprocess
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


cinemaName = ['NCHGT','NCBY','NCDG','NCWDM']
cinemaNum = [[1,2,3,4,5,6,'IMAX',8,9,10,11,12],[1,2,3,4,5,6,7],[1,2,3,4,5,6],[1,2,3,5,6,7,8,9,10,11,12,13,15,16,17]]
machineMode = ['christie','doremi','dolby']


def iterationTerm():
    resultList=[]
    zipList = zip(cinemaName,cinemaNum)
    print zipList
    for i in range(0,len(zipList)):
        listChange  = list(zipList[i])
        resultList.append(listChange.append(machineMode))
    return resultList





def lookup(cinema,hallNum,machineMode = None):
    flag1 = 0
    flag2 = 0
    flag3 = 0
    for lines in ipaddrfile:
	 #   print lines
        if cinema == lines:
            flag1 = 1
            flag2 = 0
            flag3 = 0
        if hallNum  == lines:
            flag2 = 1 
        if machineMode == lines:
            flag3 = 1       

        #	continue
#            print flag1,flag2	
#           print lines.find("IP")	
        if machineMode is None:
            if ( flag1 == 1 ) and ( flag2 == 1 ):
#                   print lines.find("IP")	
                if lines.find('IP') >= 0:		
#                       print flag1
                    flag1 = 0
                    flag2 = 0
                    flag3 = 0
#                       print flag1
            #        print lines	
            #		print lines
                    return lines.split(':')[1].strip()
        else:
            if  ( flag1 == 1 ) and ( flag2 == 1 ) and ( flag3 == 1):
                if lines.find('IP') >= 0:		
#               print flag1
                    flag1 = 0
                    flag2 = 0
                    flag3 = 0
#               print flag1
                    print lines	
                    return lines.split(':')[1].strip()
''' hallNo = argv[0]				
machineType = argv[1]				
machineIP = lookup('hallNo','machineType')
os.command('ping machineIP')
'''		
#find ip
#ip = lookup('NCHGT','DINGXIN')
#print ip
#(status,output) = commands.getstatusoutput("'ping %s' % ip")
#print status
#print output 
#os.system('ping %s' % ip)

#ping module
if __name__ == '__main__':
    listAllIn = iterationTerm()
    print listAllIn
    ip = lookup('NCBY','1','christie')
    cmd = "ping -c 3 %s" % ip
    args = shlex.split(cmd)
    print args
    try:
        subprocess.check_call(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        print 'success'
    except:
        print "fault"
    finally:
        print 'yes' 
