def main():
	a=1
	m=int(input())
	for i in range(1,m):
		a=a*i
	print(a)
try:
	main()
except:
	print('invalid')
