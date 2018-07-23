def triplet(tot,l):
	m=len(l)
	for i in range(m-2):
		for j in range(i+1,m-1):
			for k in range(j+1,m):
				if l[i]+l[j]+l[k]==tot:
					return l[i],l[j],l[k]

	return 'none'
  
def main():
	m=int(input())
	l=[]
	for i in range(m):
		l.append(int(input()))
	tot=int(input())
	print(triplet(tot,l))
try:
  main()
except:
  print('invalid')
