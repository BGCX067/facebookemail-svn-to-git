'''
Created on Jul 26, 2012

@author: aakashj
'''

count = 0

def updateSent(filename):
    fpr = open(filename,'r')
    ids = fpr.readlines()
    fpr.close()
    fpw = open(filename,'w')
    
    for line in ids:
        #print line
        data = line.split(",")
        numSent = int(data[2])
        if numSent == count:
            numSent += 1
        data[2] = str(numSent)
        fpw.write(data[0] + "," + data[1] + "," + data[2] + "\n")

    print "done"


if __name__ == '__main__':
    idfile = "d:\\temp\\fbEastBangalore.txt"
    
    updateSent(idfile)