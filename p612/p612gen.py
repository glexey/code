from random import randint
n=1000000
k=134648
print n, k
for _ in xrange(n):
    a=sorted([randint(-1e9,1e9),randint(-1e9,1e9)])
    print a[0], a[1]
