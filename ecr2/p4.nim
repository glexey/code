#import sequtils
import strutils
#from decimal import Decimal as D,getcontext
#getcontext().prec=200
#
#i=lambda:map(D,raw_input().split())
#s=lambda x:x.sqrt()
#a=lambda x:D(acos(x))
#sqrt=s
#
#x1,y1,r=i()
#x2,y2,R=i()
#if r>R:(r,R)=(R,r)
#d=s((x1-y1)**2+(x2-y2)**2)
#if d>=r+R:print 0
#elif d<=R-r:print pi*r*r
#else: print r*r*a((d*d+r*r-R*R)/2/d/r)+R*R*a((d*d+R*R-r*r)/2/d/R)-s((-d+r+R)*(d+r-R)*(d-r+R)*(d+r+R))/2

proc fscanf(c: File, frmt: cstring) {.varargs, importc, header: "<stdio.h>".}

var x1,y1,r = 0'f64
fscanf(stdin, "%lf %lf %lf", addr x1, addr y1, addr r)
echo x1, " ", y1, " ", r
