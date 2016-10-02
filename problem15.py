"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""

def fact(n):
	if n == 0:
		return 1
	else:
		return n*fact(n-1)

def nCr(n,r):
	return fact(n)/fact(n-r)/fact(r)

def numOfRoutes(l):
	return nCr(2*l,l)

print numOfRoutes(20)