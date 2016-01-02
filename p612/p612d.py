from heapq import heappush,heappop
import sys
n,k=map(int,raw_input().split())
ss=dict()
h=[]
for i in sys.stdin.readlines():
    s, e = map(int,i.split())
    if s in ss:
        ss[s] += 1
    else:
        ss[s] = 1
    if e in ss:
        ss[e] -= 1
    else:
        ss[e] = -1
    heappush(h, s)
    heappush(h, e)
m=0
ans=[]
prev = None
while h:
    x = heappop(h)
    if x == prev: continue
    prev = x
    v = ss[x]
    m += v
    if (len(ans) % 2 == 0 and m >= k) or (len(ans) % 2 != 0 and m < k):
        ans.append(x)
j=len(ans)/2
print j
for i in xrange(j):
    print ans[i*2], ans[i*2+1]
