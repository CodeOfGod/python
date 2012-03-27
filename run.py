#!/usr/bin/python
import os
import sys

if len(sys.argv)==1:
    print "please offer argv"
    sys.exit()
cmd = "java edu/bit/dlde/pageAnalysis/utils/Run "
cmd+=sys.argv[1]
print 'excute command %s ...' % cmd
