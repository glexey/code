def f(s, m):
    ans = 0
    if int(s) > m: ans += 1 # whole number
    if len(s) == 1: return ans
    for k in xrange(1, len(s)):
        if s[k] == '0': continue
        l = int(s[:k])
        if l > m:
            ans = (ans + f(s[k:], l)) % 1000000007;
    return ans

input()
print f(raw_input(), 0)
