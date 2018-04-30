# Uses python3
import sys

def period_count(m):
	"""
	Function to get the periodicity for the given modulo value
	"""
	a,b = 0,1
	for i in range (m*m):
		c = (a+b)%m
		a = b
		b = c
		if b == 1 and a == 0:
			return i+1
		
def get_fibonacci_huge_naive(n, m):
	#Get the periodicity for the modulo number
	period = period_count(m)
	
	#Finding the fibonnaci number which will give equivalent value as n%m
	#when modulo operation is performed on it with m
	num = n%period
	
	#Creating fibonnaci series to get the number
	ar = [0,1]
	for i in range (2,num+1):
		ar.append(ar[i-1]+ar[i-2])
	return ar[num] % m


n, m = map(int, sys.stdin.readline().split())
print(get_fibonacci_huge_naive(n, m))
