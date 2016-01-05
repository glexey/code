import sys
from random import randint
n,m=map(int,sys.argv[1:])
used=set()
print n,m
for i in xrange(m):
    while True:
        a,b = randint(1,n), randint(1,n)
        if (a,b) not in used:
            print a,b
            used.add((a,b))
            break
