m=int(input())
n=int(input())
o=0
while True:
    m=m+1
    if m%2==0:
        p=0
    elif m>=n:
        break
    else:
        o+=1
print(o)
