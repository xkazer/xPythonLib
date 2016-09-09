# -*- coding: UTF-8 -*-

import sys, getopt
import binascii

g_key="key"

def getFileName(path):
    try:
        return path[path.rindex('\\')+1:]
    except:
        return path

def encode(data):
    global g_key
    
    strEncode=""
    for c in data:
        strEncode += binascii.b2a_hex(chr(ord(c)^ord(g_key[0:1])))
        
    return strEncode
    
def decode(data):
    global g_key
    
    strDecode=""
    strData=binascii.a2b_hex(data)
    for c in strData:
        strDecode += chr(ord(c)^ord(g_key[0:1]))
        
    return strDecode
        
def printUsage():
    print "Useage: ", getFileName(sys.argv[0]), "[-h] [-f filename]"

if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "he:d:k:")
    iMode=0
    strData="Encode"
    for op, value in opts:
        if op == "-h":
            printUsage()
        elif op == "-e":
            strData=value
        elif op == "-d":
            iMode=1
            strData=value
        elif op == "-k":
            g_key=value
            
    if 1==iMode:
        print decode(strData)
    else:
        print encode(strData).upper()