from collections import deque
def ii(): return map(int,raw_input().split())
n,m = ii()
g = [[[] for i in xrange(m+1)] for j in xrange(n+1)]
for _ in xrange(m):
    a, b, c = ii()
    g[a][c].append(b)
    g[b][c].append(a)
q = input()
for _ in xrange(q):
    u, v = ii()
    ans = 0
    for c in xrange(1,m+1):
        vis = [False] * (n+1)
        q = deque(g[u][c])
        while(q):
            k = q.pop()
            if vis[k]: continue
            vis[k] = True
            if k == v:
                ans += 1
                break
            q.extend(g[k][c])
    print ans
