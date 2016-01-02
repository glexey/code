n,m=map(int,raw_input().split())
v = map(int,raw_input().split())

l, r, s, ans = 0, 0, 0, 0
while r < n:
    s += v[r]
    while s > m:
        s -= v[l]
        l += 1
        if l > r:
            r = l-1
            break
    r += 1
    ans = max(ans, s)
    if ans == m: break

print ans
