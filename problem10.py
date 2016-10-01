"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def sumOfPrimes(limit):
	isPrime = [True]*limit
	
	for i in range(2,limit//2):
		if isPrime[i]:
			j = 2*i
			while j < limit:
				isPrime[j] = False;
				j+=i

	sum = 0
	for i in range(2,limit):
		if isPrime[i]:
			sum += i
	return sum

print sumOfPrimes(2000000)