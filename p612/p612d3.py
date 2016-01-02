import sys
n,k=map(int,input().split())
ss=[0]*n
ee=[0]*(n+1); ee[n]=int(2e9)
for i,inp in enumerate(sys.stdin.readlines()):
    s, e = map(int,inp.split())
    ss[i] = s
    ee[i] = e
ss.sort()
ee.sort()
m,i,j,p=0,0,0,0
s = ""
while j<n:
    if i<n and ss[i] <= ee[j]:
        x = ss[i]
        while True:
            i += 1
            m += 1
            if m == k:
                s += str(x) + ' '
            if i==n or ss[i] != x: break
        while ee[j] == x:
            if m == k:
                s += str(x) + '\n'
                p += 1
            j += 1
            m -= 1
    else:
        x = ee[j]
        while True:
            if m == k:
                s += str(x) + '\n'
                p += 1
            j += 1
            m -= 1
            if x != ee[j]: break
print(p)
print(s)
