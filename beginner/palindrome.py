n=int(input("Enter number:"))
temp=n
rever=0
while(n>0):
    dig=n%10
    rever=rever*10+dig
    n=n//10
if(temp==rever):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
