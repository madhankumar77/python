def max(l):
	a=-1
	for i in l:
		if a<i:
			a=i
	print(a)
	return a
  
def main():
	n=int(input())
	l=[]
	f=0
	for i in range(n):
		l.append(int(input()))
	a=max(l)
	print(a+n)
  
main()
