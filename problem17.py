"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

def numberOfLetters(n):
	count = 0
	ones = n%10
	tens = (n//10)%10

	if tens != 1:
		if ones == 1 or ones == 2 or ones == 6:
			count+=3
		elif ones == 3 or ones == 8 or ones == 7:
			count+=5
		elif ones != 0:
			count+=4
	else:
		if ones == 0:
			count+=3
		elif ones == 1 or ones == 2:
			count+=6
		elif ones == 7:
			count+=9
		elif ones == 5 or ones ==6:
			count+=7
		else:
			count+=8

	if tens == 2 or tens == 3 or tens == 8 or tens == 9:
		count+=6
	elif tens == 7:
		count+=7
	elif tens !=1 and tens != 0:
		count+=5

	if n > 99:
		count+=numberOfLetters(n//100)+7
		if n%100 != 0:
			count+=3

	if n == 1000:
		return 11
	return count

def numberCounts(n):
	sum = 0
	for i in range(1,n+1):
		sum+=numberOfLetters(i)
	return sum

print numberCounts(1000)