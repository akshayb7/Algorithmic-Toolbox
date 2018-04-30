# Uses python3
import sys

def old_ptimal_sequence(n):
	sequence = []
	while n >= 1:
		sequence.append(n)
		if n % 3 == 0:
			n = n // 3
		elif n % 2 == 0:
			n = n // 2
		else:
			n = n - 1
	return reversed(sequence)

def optimal_sequence(n):
	""" 
	The function tries to find the optimal way to get a value 'n' from 1 by either of
	multiplication by 2 or 3, or addition of 1 to the previous number, starting from 1.
	"""
	step_value = [] #To store the middle terms encountered
	sequence = [0]*(n+1)
	#Memorizing the steps required to reach the intermediate terms
	sequence[1] = 0
	for i in range(2, n+1):
		sequence[i] = sequence[i-1]+1
		if i%2 == 0:
			sequence[i] = min(sequence[i-1]+1, sequence[i//2]+1)
		if i%3 == 0:
			sequence[i] = min(sequence[i-1]+1, sequence[i//3]+1)
		if i%2 == 0 and i%3 == 0:
			sequence[i] = min(sequence[i-1]+1, sequence[i//3]+1,sequence[i//2]+1)	
	#Finding the optimal path
	while(n>1):
		step_value.append(n)
		if(sequence[n-1] == sequence[n]-1):
			n=n-1
		elif (n%2 == 0 and sequence[n//2] == sequence[n]-1):
			n=n//2
		elif (n%3 == 0 and sequence[n//3] == sequence[n]-1):
			n=n//3
	step_value.append(1)
	return reversed(step_value)
		
n = int(sys.stdin.readline())
if n<1:
	print("Error! Please input a number greater than or equal to 1")
	exit()
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
	print(x, end=' ')
