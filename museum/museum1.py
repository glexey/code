from collections import deque

def main():
    n, m, k = [int(x) for x in input().split()]
    d0,d1,d2,d3 = -m,m-1,2,m-1
    a = []
    for _ in range(n):
        a += [(0 if v=='.' else 3) for v in input()]
    to_visit = deque()
    ans = [0,0,0,0]; n_ans = 3
    for _ in range(k):
        x0, y0 = [int(x)-1 for x in input().split()]
        i0 = x0*m+y0
        if a[i0] > 3:
            print(ans[a[i0]])
        else:
            n_ans += 1
            ans.append(0)
            to_visit.append(i0)
            while to_visit:
                i = to_visit.pop()
                a[i] = n_ans
                for d in (d0,d1,d2,d3):
                    i += d
                    if a[i] == 0:
                        to_visit.append(i)
                        a[i] = 1
                    elif a[i] == 3:
                        ans[n_ans] += 1
            print(ans[n_ans])

main()
