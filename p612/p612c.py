from collections import deque
oo = '[{<('
cc = dict(zip(oo,']}>)'))
q = deque()
ans=0
for x in raw_input():
    if x in oo:
        q.append(x)
    else:
        if q:
            if cc[q.pop()] != x:
                ans += 1
        else:
            q = True
            break
print 'Impossible' if q else ans
