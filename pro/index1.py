 def minimum(l,s,e):
	minimum=999
	for i in range(s,e+1):
		if minimum>l[i]:
			minimum=l[i]
	return minimum
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
		out.append(minimum(l,s,e))
	for i in out:
		print(i)
    
try:
  main()
except:
  print('invalid')
