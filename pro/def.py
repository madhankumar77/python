def stair():
	m=0
	n=[]
	o=int(input())
	for i in range(o):
		n.append(int(input()))
	for i in n:
		m+=(o-i)
	print(m)
  
try:
  stair()
except:
  print('invalid')
  
