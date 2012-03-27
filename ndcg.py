#!/usr/bin/python
'''This script is used to get NDCG@k with file containing records of ranked ground turth to queries and k as input. See paper "Gradient descent optimization of smoothed information retrieval metrics" for more details'''
import sys
import math
import copy
import re

def get_max_ndcg(k, *ins):
    '''This is a function to get maxium value of DCG@k. That is the DCG@k of sorted ground truth list. '''
    #print ins
    l = [i for i in ins]
    l = copy.copy(l[0])
    l.sort(None,None,True)
    #print l
    max = 0.0
    for i in range(k):
        #print l[i]/math.log(i+2,2)
        max += (math.pow(2, l[i])-1)/math.log(i+2,2)
        #max += l[i]/math.log(i+2,2)
    return max

def get_ndcg(s, k):
    '''This is a function to get ndcg '''
    z = get_max_ndcg(k, s)
    dcg = 0.0
    for i in range(k):
        #print s[i]/math.log(i+2,2)
        dcg += (math.pow(2, s[i])-1)/math.log(i+2,2)
        #dcg += s[i]/math.log(i+2,2)
    if z ==0:
        z = 1;
    ndcg = dcg/z
    #print "Line:%s, NDCG@%d is %f with DCG = %f, z = %f"%(s, k, ndcg,dcg, z)
    return ndcg

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
        if len(line)<(4*k-1):
            continue;
        arrays = re.split(r" ",line)
        #print arrays
        s = [float(i) for i in arrays]
        #print s
        get_ndcg(s, k)

##
## here is the main function
##
if __name__ == '__main__':
    test()
