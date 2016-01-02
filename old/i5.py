n = input()
i,t,s = [0] * 3
r = []
while 1 > 0:
    i += 1
    n -= i * i
    if n < 0 : break
    t += i
    m = n // t
    print "i=%d n=%d t=%d m=%d"%(i, n, t, m)
    if  m * t != n :  continue
    r.append((i, m + i))
    print "    >>> %d, %d"%(i, m+i)
    if m > 0:
        r.append((m+i, i))  

print "-----------\n"
print len(r)
r.sort()
for a in r:
    print("%d %d" % a)
