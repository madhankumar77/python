m=int(input())
print("0" if m>0 and (m & (m-1))==0 else "1")
