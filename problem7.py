"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def nthPrime(n):
	x = 1
	primes = []
	while(len(primes) < n):
		x += 1
		for y in primes:
			if x % y == 0:
				break
		else:
			primes.append(x)
	return x

print(nthPrime(10001))