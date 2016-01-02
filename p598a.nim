import math
import strutils
let t = parseInt(readLine(stdin))
for i in countup(1,t):
   let n = parseInt(readLine(stdin))
   echo int(n*(n+1) shr 1) - (4 shl int(log2(float(n)))) + 2
