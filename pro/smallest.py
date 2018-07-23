i=input("\nEnter the N number")
j=input("\nEnter the K number")
k=list(str(i))
l=j
while l>0:
    l=l-1
    del(k[l])
print(''.join(k))
