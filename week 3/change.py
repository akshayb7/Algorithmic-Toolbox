# Uses python3
import sys

def get_change(m):
	"""Function to get the minimum number of coins needed to change the input value
	(an integer) into coins with denominations 1, 5, and 10.
	"""
	coins = 0
	for i in [10,5,1]:
		if m>=i:
			coins = coins + m//i
			m = m%i
	return coins		

m = int(sys.stdin.readline())
print(get_change(m))
