"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math
def productabc():

	for x in range(math.ceil(math.sqrt(250)), math.ceil(math.sqrt(500))):
		if (500-x*x)%x == 0:
			n = x
			m = (500-x*x)//x
			break
	return 2*m*n*(n**4-m**4)

print(productabc())