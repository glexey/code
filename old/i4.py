n=int(input())
h=[int(x) for x in raw_input().split()]
amin=[0 for x in range(n)]
amax=[0 for x in range(n)]
mmin = 1e10
mmax = 0
for i in range(n):
    mmax = max(mmax, h[i])
    if i > 0: mmin = min(mmin, h[n-i])
    amax[i] = mmax
    amin[n-i-1] = mmin
splits = 1
for i in range(n-1):
    if amax[i] <= amin[i]:
        splits += 1
print splits
