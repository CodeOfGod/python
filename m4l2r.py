#!/usr/bin/python
'''This script is used to get all metrics with file containing records of ranked ground turth to queries and k as input. See paper "Gradient descent optimization of smoothed information retrieval metrics" for more details'''
import ndcg
import ap
import sys
import re
import p

##
## here is the main function
##
k=[1,3,10]
if len(sys.argv)<2:
    print "arguments missing"
    sys.exit()
f = open(sys.argv[1])
ttl1 = 0
ttl3 = 0
ttl10 = 0
p1 = 0
p3 = 0
p10 = 0 
apTtl = 0
qCount = 0
count1 = 1
count3 = 1
count10 = 1
while 1:
    line = f.readline()
    if not line:
        break;
    arrays = re.split(r" ",line)
    #print arrays
    s = [float(i) for i in arrays]
    #print s
    qCount += 1
    apTtl += ap.get_ap(s)
    for tmp_k in k:
        if len(line)<(4*tmp_k-1):
            continue;
        if tmp_k ==1:
            ttl1 += ndcg.get_ndcg(s, tmp_k)
            p1 += p.get_p(s,tmp_k)
            count1 = count1 + 1
        if tmp_k ==3:
            ttl3 += ndcg.get_ndcg(s, tmp_k)
            p3 += p.get_p(s,tmp_k)
            count3 = count3 + 1
        if tmp_k ==10:
            ttl10 += ndcg.get_ndcg(s, tmp_k)
            p10 += p.get_p(s,tmp_k)
            count10 = count10 + 1
print "NDCG@1: %f, NDCG@3: %f, NDCG@10: %f, MAP: %f"%(ttl1/count1,ttl3/count3,ttl10/count10, apTtl/qCount)
