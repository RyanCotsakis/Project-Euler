"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def largestPalindrome():
	largest = 0
	for x in range(999,99,-1):
		for y in range(999,x-1,-1):
			prod = "%i" %(x*y)
			if prod == prod[::-1] and x*y > largest:
				largest = x*y
			if y == 999 and x*y < largest:
				return largest

print(largestPalindrome())

