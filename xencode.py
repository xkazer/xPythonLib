# -*- coding: UTF-8 -*-

import sys, getopt
import binascii

EncodeMap='EADFCB7410852963'
DecodeMap=[i for i in range(256)]

def getFileName(path):
    try:
        return path[path.rindex('\\')+1:]
    except:
        return path

def encode(data, key):
    byteKey=0
    strEncode = ""
    utfStr = data.decode('GBK').encode('UTF-8')
    #print binascii.b2a_hex(utfStr)
    for char in key:
        byteKey ^= ord(char) 
    for charData in utfStr:
        chrTmp = ord(charData)^byteKey
        highData = (chrTmp>>4)&0xF
        lowData = chrTmp&0xF
        #print hex(highData), hex(lowData)
        strEncode = strEncode+EncodeMap[lowData]+EncodeMap[highData]
    return strEncode

def decode(data, key):
    byteKey=0
    strDecode = ""
    for i in range(16):
        DecodeMap[ord(EncodeMap[i])] = i

    for char in key:
        byteKey ^= ord(char)
    cur = 0
    while (cur < len(data)-1):
        highData = DecodeMap[ord(data[cur])]
        lowData = DecodeMap[ord(data[cur+1])]
        #print hex(highData), hex(lowData)
        strDecode += chr(((lowData<<4)|highData)^byteKey)
        cur += 2
    #print binascii.b2a_hex(strDecode)
    return strDecode.decode('UTF-8').encode('GBK')
        
def printUsage():
    print "Useage: ", getFileName(sys.argv[0]), "[-h] [-e|d string] [-k key]"

if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "he:d:k:")
    iMode=0
    strKey="encode"
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
            strKey=value
            
    if 1==iMode:
        print decode(strData, strKey)
    else:
        print encode(strData, strKey).upper()