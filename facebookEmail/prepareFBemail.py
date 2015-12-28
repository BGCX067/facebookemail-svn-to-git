'''
Created on Jul 26, 2012

@author: aakashj
'''

count = 0

def prepareFile(readname, writename):
    fpr = open(readname,'r')
    fpw = open(writename, 'w')
    i = 0
    for line in fpr.readlines():
        #print line
        emailid = line.split(",")[0]
        num = int(line.split(",")[2])
        if num == count:
            data = emailid + "@facebook.com,"
            fpw.write(data)
            i += 1
            if (i % 499) == 0:
                fpw.write("\n\n")
    
    print i


if __name__ == '__main__':
    idfile = "d:\\temp\\fbEastBangalore.txt"
    emailfile = "d:\\temp\\fbEmail.txt"
    
    prepareFile(idfile, emailfile)