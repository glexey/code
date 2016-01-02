x=input()*6
a=set()
m = 0
while True:
    m += 1
    m2=m*(m+1)
    n = int( (x/m2-1+m)/3 )
    if n < m: break
    if x == m2*(3*n-m+1):
        a.add((m,n))
        a.add((n,m))
print len(a)
for v in sorted(a):
    print v[0], v[1]
