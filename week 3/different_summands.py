# Uses python3
import sys

def optimal_summands(n):
	"""
	The goal of this problem is to represent a given positive integer 𝑛 as a sum of as many pairwise
	distinct positive integers as possible.
	"""
	summands = []
	for i in range(1,n+1):
		n = n-i
		#If the sum of distinct numbers is already equal to the given integer
		if n == 0:
			summands.append(i)
			break
		#If the current i is greater than remaining value of sum to reach n, 
		#then append i+n as the last distinct integer, because if we append i 
		#then last integer won't be distinct (as i>=n)
		elif n<=i:
			summands.append(n+i)
			break
		else:
			summands.append(i)
	
	return summands		

if __name__ == '__main__':
	input = sys.stdin.read()
	n = int(input)
	summands = optimal_summands(n)
	print(len(summands))
	for x in summands:
		print(x, end=' ')
