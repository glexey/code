n=input()
if n%2:
    n-=3
    ans=1+n/2
    print ans
    print "2 "*(n/2)+"3"
else:
    print n/2
    print ' '.join("2" for x in range(n/2))
