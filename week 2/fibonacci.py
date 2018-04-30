# Uses python3
def calc_fib(n):
	ar = [0,1]
	for i in range (2,n+1):
		ar.append(ar[i-1]+ar[i-2])
	return ar[n]	

n = int(input())
print(calc_fib(n))
