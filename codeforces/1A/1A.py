# Theatre Square in the capital city of Berland has a rectangular shape with the size nXm meters. On the occasion of the city's anniversary, a decision was taken to pave the Square with square granite flagstones. Each flagstone is of the size axa
# What is the least number of flagstones needed to pave the Square? It's allowed to cover the surface larger than the Theatre Square, but the Square has to be covered. It's not allowed to break the flagstones. The sides of flagstones should be parallel to the sides of the Square.

n,m,a = map(int,input().split())

if n%a==0:
	x=n//a
else:
	x=(n//a)+1
if m%a==0:
	y=m//a
else:
	y=(m//a)+1

print(x*y)