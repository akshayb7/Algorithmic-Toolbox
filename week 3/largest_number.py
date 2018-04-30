#Uses python3

import sys

def largest_number(a):
	"""
	Compose the largest number out of a set of integers.
	"""
	largest_num = ""
	for i in range(len(a)):
		for j in range(i+1, len(a)):
			str1 = str(a[i])+str(a[j])
			str2 = str(a[j])+str(a[i])
			if int(str2) > int(str1):
				temp = a[j]
				a[j] = a[i]
				a[i] = temp
	
	for i in range(len(a)):
		largest_num = largest_num + str(a[i])
	return largest_num	
	
input = sys.stdin.read()
data = input.split()
a = data[1:]
print(largest_number(a))
    
