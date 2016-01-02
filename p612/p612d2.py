from heapq import heappush,heappop
import sys
n,k=map(int,input().split())
ss=[]
ee=[]
for i in sys.stdin.readlines():
    s, e = map(int,i.split())
    heappush(ss, s)
    heappush(ee, e)
ss.sort()
ee.sort()
m,i,j,p,mm=0,0,0,0,0
s = ""
while j<n:
    # find element
    if i<n and ss[i] < ee[j]:
        x = ss[i]
    else:
        x = ee[j]
    # compare and advance
    mm = m
    while i<n and ss[i] == x:
        i += 1
        m += 1
        mm = m
    while j<n and ee[j] == x:
        j += 1
        m -= 1
    # add to answer
    if mm >= k and p % 2 == 0:
        s += str(x) + ' '
        p += 1
    if m < k and p % 2 != 0:
        s += str(x) + "\n"
        p += 1
print(p//2)
print(s)
