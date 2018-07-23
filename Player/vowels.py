def removevowels(string):
	m=len(string)
	outstring=''
	v=['a','e','i','o','u','A','E','I','O','U']
	for i in range(m):
		if string[i] in v:
			continue
		outstring+=string[i]
	print(outstr)

def main():
	try:
		str=input()
		removevowels(str)
	except:
		print('invalid')
main()
