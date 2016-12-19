s,x1,x2 = map(int, raw_input().split())
t1,t2 = map(int, raw_input().split())
p,d = map(int, raw_input().split())

# put x2 always on the right side
if x1 > x2:
    p = s - p
    d = -d
    x1, x2 = s - x1, s - x2

# distance for tram to go to x2
if d < 0:
    dist_tram = p + x2
else:
    if p < x2:
        dist_tram = x2 - p
    else:
        dist_tram = s - p + s + x2

if (x2 - x1) * t2 < dist_tram * t1:
    # Igor will come first
    print (x2 - x1) * t2
else:
    # Tram will come first, will Igor catch it?
    if p <= x1 or p > x2 or d < 0: # yes
        print dist_tram * t1
    else: # no, one more round
        dist_tram += 2 * s
        # and once again
        if (x2 - x1) * t2 < dist_tram * t1:
            # Igor will come first
            print (x2 - x1) * t2
        else:
            # Now Igor is bound to catch it
            print dist_tram * t1



