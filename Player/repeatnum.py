try:
    m = int(input())
    n1 = list(map(int,input().split(' ')))
    n2 = [0]*50
    for i in range(m):
        n2[n1[i]]+=1
    print(n2.index(1))    
except:
    print("Invalid Input")
