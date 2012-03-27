#!/usr/bin/python
'''this script is used to get AP, MAP with file containing records of ranked ground turth to queries and k as input. See paper "Gradient descent optimization of smoothed information retrieval metrics" for more details'''
import sys
import math
import copy
import re
import p

def get_ap(s):
    '''This is a function to get average precision'''
    a = 0.0
    b = 0.0
    for i in range(len(s)):
        if s[i]>0:
            a += p.get_p(s, i+1)
            b += 1
    #print "Line: %s, ap is %f with a = %f, b = %f"%(s, a/b, a, b)
    if b == 0:
        b = 1
    return a/b

def get_map(s, k):
    '''This is a function to get mean average precision'''
    a = 0.0
    for i in range(len(s)):
        if s[i]>0:
            a += 1
    #print "Line: %sp@%d is %f with a = %f"%(line, k, a/k, a)
    return a / k

def test():
    if len(sys.argv)!=2:
        print "arguments missing"
        sys.exit()
    f = open(sys.argv[1])
    while 1:
        line = f.readline()
        if not line:
            break;
        arrays = re.split(r" ",line)
        #print arrays
        s = [float(i) for i in arrays]
        #print s
        get_ap(s)

##
## here is the main function
##
if __name__ == '__main__':
    test()
