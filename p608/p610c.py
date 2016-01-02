n=input()
ab = [0 for _ in xrange(n)]
for i in xrange(n):
    ab[i] = map(int,raw_input().split())

ab = sorted(ab, key=lambda x: x[0])

# sort index of by how far left destruction spans
srt = sorted(range(n),key=lambda x:ab[x][0]-ab[x][1])

di = range(n) # index of leftmost destroyed element
yes = di[:]   # Left sum if element present
no  = di[:]   # Left sum if element not present

j = 0
for i,sid in enumerate(srt):
    while  j < n:
        if ab[sid][0]-ab[sid][1] <= ab[j][0]:
            di[sid] = j
            break
        else:
            j += 1

yes[0] = 1
for i in xrange(1,n):
    no[i] = yes[i-1]
    yes[i] = 1 + no[di[i]]

print n-max(yes)
