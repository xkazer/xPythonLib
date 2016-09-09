# -*- coding: UTF-8 -*-

import sys, getopt
import hashlib


def getFileName(path):
    try:
        return path[path.rindex('\\')+1:]
    except:
        return path
        
def calcMd5(path):
    m = hashlib.md5()
    hFile = open(path, 'rb')
    m.update(hFile.read())
    hFile.close()
    
    return m.hexdigest()

def printUsage():
    print "Useage: ", getFileName(sys.argv[0]), "[-h] [-f filename]"

if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "hf:")
    for op, value in opts:
        if op == "-h":
            printUsage()
        elif op == "-f":
            strMd5 = calcMd5(value)
            print "File:", value
            print "md5:", strMd5
            print "MD5:", strMd5.upper() 