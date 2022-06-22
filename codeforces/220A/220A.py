n=int(input())
a = list(map(int,input().strip().split()))
b = sorted(a)

swapcount = 0
for x in range(len(a)):
	if a[x] != b[x]:
		swapcount+=1

if swapcount==0 or swapcount==2:
	print("YES")
else:
	print("NO")
