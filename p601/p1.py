n, bx = [int(_) for _ in raw_input().split()]
x = [int(_) for _ in raw_input().split()]
m, by = [int(_) for _ in raw_input().split()]
y = [int(_) for _ in raw_input().split()]

xx, yy = 0, 0

for i in x:
    xx *= bx
    xx += i

for i in y:
    yy *= by
    yy += i

if xx<yy: print "<"
if xx>yy: print ">"
if xx==yy: print "="
