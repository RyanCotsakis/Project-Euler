"""
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

def factorial(n):
	if n == 0: return 1
	return factorial(n-1)*n

def lexographic(n):
	nth = []
	n = n-1
	for i in range(9,-1,-1):
		temp = int(n/factorial(i))
		n -= temp*factorial(i)
		nth.append(temp)
	available = range(10)
	ans = [0]*10
	for i in range(10):
		ans[i] = available[nth[i]]
		del available[nth[i]]
	return ans

print lexographic(1000000)

