# Uses python3
import sys

def fibonacci_partial_sum_naive(n):
	if n <= 2:
		return n
	
	#The pisano period of modulo by 10 is 60
	num = n%60
	if num == 0:
		sum = 0
	else:
		sum = 1
	div = int(n/60)
	
	ar = [0,1]
	for i in range (2,num+1):
		ar.append((ar[i-1]+ar[i-2])%10)
		sum = sum + ar[i]
	
	
	return sum%10


from_, to = map(int, sys.stdin.readline().split())
n = fibonacci_partial_sum_naive(to)
m = fibonacci_partial_sum_naive(from_-1)
if n-m<0:
	print(10+n-m)
else:
	print (n-m)