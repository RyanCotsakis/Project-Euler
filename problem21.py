"""
Evaluate the sum of all the amicable numbers under 10000.
"""

def sumOfFactors(n):
	factors = [i for i in range(1,n) if n%i == 0]
	return sum(factors)

def aimicableNumbers(n):
	aimicableNumbers = [0]*(n-1)
	runningCount = 0
	for i in range(1,n):
		sumFacts = sumOfFactors(i)
		if sumFacts > i:
			aimicableNumbers[i] = sumFacts
		elif sumFacts < i and aimicableNumbers[sumFacts] == i:
			runningCount += sumFacts + i
	return runningCount

print aimicableNumbers(10000)




