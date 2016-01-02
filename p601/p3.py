from sys import exit

n, m = [int(x) for x in raw_input().split()]
uv = [[int(x)-1 for x in raw_input().split()] for _ in range(m)]

dt = [[_] for _ in range(n)]
for u,v in uv:
    dt[u].append(v)
    dt[v].append(u)

db = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if j not in dt[i]:
            db[i].append(j)

def get_next(bc, tc, visited):
    nxt = []
    bchoice = db[bc] if bc != n-1 else [bc]
    tchoice = dt[tc] if tc != n-1 else [tc]
    for bn in bchoice:
        for tn in tchoice:
            if bn == n-1 and tn == n-1:
                return 1
            if bn == bc and tn == tc: continue
            if bn == tn: continue
            if (bn, tn) in visited: continue
            nxt.append((bn, tn))
    return nxt

visited = set()

steps=[(0,0)]
i = 0
while len(steps) > 0:
    i += 1
    cur_level = steps[:]
    steps = []
    for bc,tc in cur_level:
        visited.add((bc, tc))
        nxt = get_next(bc, tc, visited)
        if nxt == 1:
            print i
            exit()
        steps += nxt

print -1
