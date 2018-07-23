def sumdigsqr(n1):
	sum1=0
	while(n1!=0):
		r1=n1%10
		sum1+=r1*r1
		n1//=10
	return sum1
def happy(n1):
	while(n1>0):
		n=sumdigsqr(n1)
		if n1==1:
			print('happy number')
			return
	print('not happy number')
def main():
	try:
		n1=int(input())
		happy(n1)
	except:
		print('invalid')
main()
