m=list(input())
n=list(input())
o=len(a)
p=0
i=0
while o>0:
    p=p+(ord(n[i])-ord(m[i]))
    i=i+1
    o=o-1
print(p)
