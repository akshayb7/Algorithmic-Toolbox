# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
	"""
	Function to give the optimal value of items stored in a 
	knapsack allowing fractional items.
	"""
	value = 0.
	length = len(weights)
	val_by_wt = [0]*length
	for i in range(length):
		val_by_wt[i]= values[i]/weights[i]
	for i in range(length):
		for j in range(i+1,length):
			if(val_by_wt[i] < val_by_wt[j]):
				temp =val_by_wt[i]
				val_by_wt[i] = val_by_wt[j]
				val_by_wt[j] = temp
				temp = weights[i]
				weights[i] = weights[j]
				weights[j] = temp
				
	for i in range(length):
		if(capacity == 0):
			break
		elif(capacity >= weights[i]):
			value = value + (weights[i]*val_by_wt[i])
			capacity = capacity - weights[i]
		else:
			value = value + (capacity*val_by_wt[i])
			capacity = 0
	return value		

n, capacity = 3,50
values = [60,100,120]
weights = [20,50,30]
opt_value = get_optimal_value(capacity, weights, values)
print("{:.10f}".format(opt_value))
