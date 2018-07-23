m=list(input())
n=list(input())
o=len(a)
p=len(b)
i=0
j=0
o=[]
while p>0:
    if m[i]==n[j]:
        o.append(m[i])
    j=j+1
    i=i+1
    p=p-1
print(p-len(o))
