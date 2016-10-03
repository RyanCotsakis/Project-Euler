"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def powSum(n):
	answer = ['1']
	carry = 0
	for i in range(n):
		for (j,digit) in enumerate(answer):
			newDigit = int(digit)*2 + carry
			answer[j]=str((newDigit)%10)
			carry = newDigit//10
		while carry > 0:
			answer = answer + [str(carry%10)]
			carry = carry//10
	return sum([int(i) for i in answer])

print powSum(1000)