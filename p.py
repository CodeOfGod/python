#!/usr/bin/python
'''This script is used to get P@k with file containing records of ranked ground turth to queries and k as input. See paper "Gradient descent optimization of smoothed information retrieval metrics" for more details'''
import sys
import re

def get_p(s, k):
    '''This is a function to get precision when we treat doc with relevance higher than 0 as a relevant one and doc with relevance equal 0 as irrelevant'''
    a = 0.0
    for i in range(k):
        if s[i]>0:
            a += 1
    #print "Line: %s, p@%d is %f with a = %f"%(s, k, a/k, a)
    return a / k

def test():
    if len(sys.argv)!=3:
        print "arguments missing"
        sys.exit()
    k = int(sys.argv[2])
    f = open(sys.argv[1])
    while 1:
        line = f.readline()
        if not line:
            break;
        arrays = re.split(r" ",line)
        #print arrays
        s = [float(i) for i in arrays]
        #print s
        get_p(s, k)

##
## here is the main function
##
if __name__ == '__main__':
    test()

