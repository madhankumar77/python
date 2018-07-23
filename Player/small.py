 def small(string):
	a=0
	b=[]
	c=list(string)
	for i in range(len(l)):
		if a==3:
			a=0
			b.append('.')
		b.append(l[i])
		a+=1
	return(''.join(b))
	
 def f():
	fin=[]
	st=input('Enter your address:\n')
	str=list(st)
	str.insert(3,".")
	str.insert(7,".")
	str.insert(10,".")
	fin.append( (''.join(str)))
	fin.append(small(st))
	print(fin)
	
f()
