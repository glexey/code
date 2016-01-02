d1,d2,d3 = [int(x) for x in raw_input().split()]
r = [
        d1 + d3*2 + d1,
        d2 + d3*2 + d2,
        d1 + d2 + d3,
        d1 * 2 + d2 * 2
        ]
print min(r)
