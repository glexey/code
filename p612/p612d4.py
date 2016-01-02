import sys
n,k=map(int,input().split())
a=[0]*n*2
i=0
for inp in sys.stdin.readlines():
    s, e = map(int,inp.split())
    a[i] = (s,False)
    i += 1
    a[i] = (e,True)
    i += 1
a.sort()
m,p=0,0
ans = ""
for x in a:
    if x[1]:
        if m == k:
            ans += str(x[0]) + "\n"
            p += 1
        m -= 1
    else:
        m += 1
        if m == k:
            ans += str(x[0]) + ' '
print(p)
print(ans)
