try:
	s1=raw_input()
	m=s1.split(' ')
	g=" "
	for i in range(0,len(m)):
			m[i]=m[i].capitalize()
	n=m[0]
	for i in range(1,len(m)):
		n=n+g+m[i]
	print n
except:
	print "Invalid"
