from random import randint

n=20
m=20
k=1

print n, m, k
print '*'*m
for _ in xrange(n-2):
    print '*' + '.'*(m-2) + '*'
print '*'*m
for _ in xrange(k):
    print randint(2,n-1), randint(2,m-1)
