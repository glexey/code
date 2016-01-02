a=raw_input()
b=raw_input()
la=len(a)
lb=len(b)
s0 = [0 for _ in xrange(la)]
s0[0] = b[:lb-la+1].count('0')
s1 = s0[:]
s1[0] = b[:lb-la+1].count('1')
for i in xrange(1,la):
    if b[lb-la+i] == '0':
        s1[i] = s1[i-1]
        s0[i] = s0[i-1] + 1
    else:
        s1[i] = s1[i-1] + 1
        s0[i] = s0[i-1]
    if b[i-1] == '0':
        s0[i] -= 1
    else:
        s1[i] -= 1
#print s0, s1
ans = 0
for i in xrange(la):
    if a[i] == '0':
        ans += s1[i]
    else:
        ans += s0[i]
print ans
