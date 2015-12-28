'''
Created on Jul 26, 2012

@author: aakashj
'''


import re
import urllib2
#import time



emailHash = {}

def extractEmail(data):
    p = re.compile('facebook\.com\/[0-9a-zA-Z.]+[\"|\?]')
    q = re.compile('facebook\.com\\\/[0-9a-zA-Z.]+[\"|\?]')
    try:
        #data = urllib2.urlopen(url)
        for line in data:
            m = p.findall(line)
            for i in m:
                j = i.split("/")
                emailid = j[1][:-1]
                #print emailid + "@facebook.com"
                if emailid in emailHash:
                    emailHash[emailid][0] += 1
                else:
                    print emailid
                    emailHash[emailid] = [1,0]
                    
    
        for line in  data:
            m = q.findall(line)
            for i in m:
                j = i.split("/")
                emailid = j[1][:-1]
                #print emailid + "@facebook.com"
                if emailid in emailHash:
                    emailHash[emailid][0] += 1
                else:
                    print emailid
                    emailHash[emailid] = [1,0]
    except:
        pass
    

def extractEmailfromURLs(filename):
    fp = open(filename)
    urls = fp.readlines()
    try:
        for url in urls:
            print url
            data = urllib2.urlopen(url)
            extractEmail(data)
    except:
        pass
    
    
def extractEmailfromURL(url):
    print url
    try:
        data = urllib2.urlopen(url)
        extractEmail(data)
    except:
        pass
    
def extractEmailfromFile(filename):
    fp = open(filename)
    data = fp.readlines()
    extractEmail(data)


def extractFBemailfromPhoto(filename):
    fp = open(filename, 'r')
#p = re.compile('facebook\.com\/[0-9a-z.]+(\"|\?)')
    r = re.compile('https?:\/\/www\.facebook\.com\/photo\.php\?[\w\d\=\&\.;]+\"')
#p = re.compile('facebook\.com\\\/[0-9a-z.]+[\"|\?]')

    urls = fp.readlines()
    try:
        for url in  urls:
            print url
            data = urllib2.urlopen(url)
            for line in data:
                photoUrls = r.findall(line)
                for u in photoUrls:
                    print u
                    extractEmailfromURL(u)
    except:
        pass
                    
    #print emailHash
    
    
    
def writeFBemailFile(filename):
    fp = open(filename, 'w')
    for emailid in emailHash:
        data = emailid + "," + str(emailHash[emailid][0]) + "," + str(emailHash[emailid][1]) + "\n"
        fp.write(data)
        
def readFBemailFile(filename):
    fp = open(filename, "r+")
    #print fp.readlines()
    for line in fp.readlines():
        #print line
        emailid = line.split(",")
        #print emailid
        count = int(emailid[1])
        numSent = int(emailid[2])
        emailid = emailid[0]
        emailHash[emailid] = [count,numSent]
    
    print emailHash
    fp.close()
        


if __name__ == '__main__':
    tempFB = "d:\\temp\\tempFB.txt"
    emailfile = "d:\\temp\\fbHisar.txt"
    readFBemailFile(emailfile)
    #filetime = os.stat(tempFB).st_mtime
    #newfiletime = os.stat(tempFB).st_mtime
    
    #while 1:
        #if (filetime != (newfiletime = os.stat(tempFB).st_mtime)):
            #time.sleep(2)
            #print "file has changed."
    #extractFBemail(tempFB)
    extractEmailfromFile(tempFB)
    #extractEmailfromURLs(tempFB)
    #extractEmail("https://www.facebook.com/browse/event_members/?id=329613077126640&edge=temporal_groups%3Amember_of_temporal_group&showstatus=0")
    writeFBemailFile(emailfile)
            #filetime = os.stat(tempFB).st_mtime
            #print "done."
    
    
    