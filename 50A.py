m,n=map(int,input().split())
if n%2 != 0 and m%2 != 0:
	x=(m*n)//2
else:
	x=(m*n)/2
print(int (x))