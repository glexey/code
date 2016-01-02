n=input()
b=raw_input()
a = 1
l = b[0]
for i in range(1,n):
    if b[i] != l:
        a += 1
print min(a+2,n)
