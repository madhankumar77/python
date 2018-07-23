def xor(l,s,e):
	n=0
	for i in range(s-1,e):
		n=n^l[i]
	return n
def main():
	n=int(input())
	l=[]
	for i in range(n):
		l.append(int(input()))
	q=int(input())
	out=[]
	for i in range(q):
		s=int(input())
		e=int(input())
		out.append(xor(l,s,e))
	for i in out:
		print(i)
    
try:
  main()
excpet:
  print('invalid')
