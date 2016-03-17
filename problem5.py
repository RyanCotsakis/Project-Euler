"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def smallestMultiple():
	factors = []
	for x in range(2,21):
		factor = x
		for y in factors:
			if factor%y == 0:
				factor//=y
		factors.append(factor)
	smallestMultiple = 1
	for factor in factors:
		smallestMultiple*=factor
	return smallestMultiple

print(smallestMultiple())