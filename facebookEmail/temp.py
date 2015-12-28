'''
Created on Jul 26, 2012

@author: aakashj
'''

import urllib2
import re


if __name__ == '__main__':
    
    #data = urllib2.urlopen('https://www.facebook.com/browse/event_members/?id=329613077126640')
    #p = re.compile('https?:\/\/www\.facebook\.com\/[\w\d\=\&\.;]+\"')
    fp = open("d:\\temp\\tempFB.txt")
    data = fp.readlines()
    p = re.compile('facebook\.com\/[0-9a-z.]+[\"|\?]')
    
    for line in data:
        #print line
        #line = 'href="http://www.facebook.com/photo.php?fbid=378817785517268&amp;set=a.378817598850620.86529.147207215344994&amp;type=3" aria-label="Photo" name="378817785517268"'
        m = p.findall(line)
        print m
        
    #filename = "d:\\temp\\tempFB.txt"
    #filetime = os.stat(filename).st_mtime
    
    #while 1:
        #if (filetime != os.stat(filename).st_mtime):
            #print "file has changed."
            #filetime = os.stat(filename).st_mtime
    
    
    