x,y,z= map(int,input().split())
if z>=x+y:
	print(z-(x+y)+1)
elif y>=x+z:
	print(y-(x+z)+1)
elif x>=y+z:
	print(x-(y+z)+1)
else:
	print(0)
