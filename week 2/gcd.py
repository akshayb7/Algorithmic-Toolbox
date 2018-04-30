# Uses python3
import sys
def gcd_naive(a, b):
	smaller_num = min(a,b)
	bigger_num = max(a,b)
	if bigger_num % smaller_num == 0:
		return smaller_num
	else:
		return gcd_naive(smaller_num, bigger_num % smaller_num)

a, b = map(int, sys.stdin.readline().split())
print(gcd_naive(a, b))
