from collections import deque

def main():
    n, m, k = [int(x) for x in input().split()]
    d0,d1,d2,d3 = -m,m-1,2,m-1
    a = []
    for _ in range(n):
        a += [(0 if v=='.' else 3) for v in input()]
    to_visit = deque()
    for _ in range(k):
        x0, y0 = [int(x)-1 for x in input().split()]
        i0 = x0*m+y0
        if a[i0] > 3:
            print(a[i0])
        else:
            sum = 0
            to_visit.append(i0)
            visited = deque()
            while to_visit:
                i = to_visit.pop()
                visited.append(i)
                a[i]=2
                i += d0
                if a[i] == 0:
                    to_visit.append(i)
                    a[i] = 1
                elif a[i] == 3: sum += 1
                i += d1
                if a[i] == 0:
                    to_visit.append(i)
                    a[i] = 1
                elif a[i] == 3: sum += 1
                i += d2
                if a[i] == 0:
                    to_visit.append(i)
                    a[i] = 1
                elif a[i] == 3: sum += 1
                i += d3
                if a[i] == 0:
                    to_visit.append(i)
                    a[i] = 1
                elif a[i] == 3: sum += 1
            print(sum)
            for i in visited:
                a[i] = sum

main()
