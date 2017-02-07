"""
Find the sum of the digits in the number 100!
"""

def multiplyToString(mylist, n):
	mylist = mylist[::-1]
	ans = []
	carry = 0
	for i in mylist:
		digit = i*n
		carry,b = divmod(digit+carry,10)
		ans.append(b)
	ans = ans[::-1]
	if carry != 0:
		ans = [int(d) for d in str(carry)] + ans
	return ans


def sumFactorial(n):
	ans = [1]
	for i in range(1,n+1):
		ans = multiplyToString(ans,i)
	return sum(ans)

print sumFactorial(100)