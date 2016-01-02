n=input()
c=map(int,raw_input().split())
ss={}
def s(l,r):
    if r<l: return 0
    if r==l: return 1
    if (l,r) in ss: return ss[l,r]
    ans = 1+s(l+(2 if c[l] == c[l+1] else 1), r)
    for x in xrange(l+2, r+1):
        if c[x] == c[l]:
            ans = min(ans, s(l+1, x-1) + s(x+1, r))
    ss[l,r] = ans
    return ans

print s(0,n-1)
