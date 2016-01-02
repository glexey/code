from collections import deque
n,m=map(int,raw_input().split())
a=[set() for i in range(n+1)]
for i in range(m):
    x,y=map(int,raw_input().split())  
    a[x].add(y)
    a[y].add(x)
t = n not in a[1] # no direct railway from 1 to n
q=deque()
q.append(1)
z = [-1 for i in range(n+1)]
z[1] = 0
print a
while len(q) > 0:
    v = q.popleft()
    print "train/bus at", v
    for i in range(1, n+1):
        if t ^ (i in a[v]):
            continue
        if z[i]==-1:
            z[i]=z[v]+1
            q.append(i)
            if i == n:
                print(z[i])
                exit(0)
    print ">> q,z:", q, z
print(-1) 
