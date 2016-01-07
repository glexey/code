import sys
from random import randint
x = lambda: randint(1, 1000000000)
n, m, k = map(int,sys.argv[1:])
print n, m, k, x()
for _ in xrange(n):
    print x(), x()
