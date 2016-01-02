from collections import deque

w=32

def disp(a, n, m, I=None):
    l = ""
    for x in range(n):
        for y in range(m):
            i = x*m + y
            if I == i:
                l += "X"
            elif a[i] == 0:
                l += "."
            elif a[i] == 1:
                l += "-"
            elif a[i] == 2:
                l += "v"
            else:
                l += "*"
        l += "\n"
    return l[:-1]

def empty_around(i, rc, n, m, nw, mw):
    r = (i//m)//w;
    c = (i%m)//w;
    j = r*mw+c
    if j < len(rc):
        if rc[j] == 0:
            rc[j] = 1
            return True, r, c
    return False, 0, 0

def fill_around(a, r0, c0, to_visit, visited, n, m):
    for r in range(w):
        for c in range(w):
            i = (r0*w + r)*m + (c0*w + c)
            if (r==0 or r==w-1 or c==0 or c==w-1):
                if a[i] == 0:
                    to_visit.append(i)
                    a[i] = 1
            else:
                a[i] = 2
                visited.append(i)

def main():
    n, m, k = [int(x) for x in input().split()]
    d0,d1,d2,d3 = -m,2*m,-m-1,2
    a = []
    rc = [] # column-reduced version
    rr = [] # fully-reduced version
    mw = m//w
    nw = n//w
    for _ in range(n):
        row = [(0 if v=='.' else 3) for v in input()]
        a += row
        rc += [sum(row[i*w:i*w+w]) for i in range(mw)]
    for i in range(nw): # row number in fully reduced array
        j = i*mw*w # first cell in column-reduced array
        rr += [sum([rc[j+u*mw+v] for u in range(w)]) for v in range(mw)]
    to_visit = deque()
    for _ in range(k):
        x0, y0 = [int(x)-1 for x in input().split()]
        i0 = x0*m+y0
        step = 0
        if a[i0] > 3:
            print(a[i0])
        else:
            ans = 0
            to_visit.append(i0)
            visited = deque()
            step += 1
            while to_visit:
                i = to_visit.pop()
                if a[i] == 2: continue # only required with reduction
                visited.append(i)
                if step % w == 1:
                    e, r0, c0 = empty_around(i, rr, n, m, nw, mw)
                else:
                    e = False
                a[i]=2
                if e:
                    fill_around(a, r0, c0, to_visit, visited, n, m)
                for d in (d0,d1,d2,d3):
                    i += d
                    if a[i] == 0:
                        to_visit.append(i)
                        a[i] = 1
                    elif a[i] == 3:
                        ans += 1
            print(ans)
            for i in visited:
                a[i] = ans

main()
