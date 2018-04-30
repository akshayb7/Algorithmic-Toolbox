# Uses python3
import sys

def get_majority_element(a, left, right):
	if left == right:
		return -1
	if left + 1 == right:
		return a[left]
	a.sort()
	count = 0
	element = a[0]
	for i in range(len(a)):
		if(a[i]==element):
			count=count+1
		else:
			element=a[i]
			count=1
		if(count>(len(a)/2)):
			return 1
	return -1

input = sys.stdin.read()
n, *a = list(map(int, input.split()))
if get_majority_element(a, 0, n) != -1:
	print(1)
else:
	print(0)
