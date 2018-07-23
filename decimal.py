def main():
	m=int(input())
	l=[]
	for i in range(m):
		l.append(int(input()))
	l.sort(reverse=True)
	for i in l:
		print(i)
try:
  main()
except:
  print('invalid')
