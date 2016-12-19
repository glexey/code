n=input()
s=raw_input()
print s[-2::-2]+s[1-n%2::2]
