try :
	str1=raw_input("time (hh:mm) : ")
	str2=raw_input("time (hh:mm) : ")
	ans=0
	m=str1.split(':')
	n=str2.split(':')
	o=int(m[0])*60+int(m[1])
	p=int(n[0])*60+int(n[1])
	if(o>p):
		ans=o-p
	else:
		ans=p-o
	print ans
except :
	print "Invalid"
