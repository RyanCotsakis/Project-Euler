"""
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

def isAbundant(n):
	factors = [i for i in range(1,n) if n%i == 0]
	return sum(factors) > n

def mySum():
	abundantNumbers = [i for i in range(1,28123) if isAbundant(i)]
	allNums = [i for i in range(28123)]
	for i in abundantNumbers:
		for j in abundantNumbers:
			if i+j < 28123:
				allNums[i+j] = 0
	return sum(allNums)

print mySum()