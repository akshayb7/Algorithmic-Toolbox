# Uses python3
import sys

def optimal_weight(W, w):
	"""
	Function to implement the knapsack problem without repetition
	"""
	#Memorizing the values for each weight up to W
	store = [0]*(W+1) #Initializing all stored weight initially to zero
	for i in range(len(w)):
		for weight in range(W, w[i]-1, -1):
			#Memorizing the maximum stored weight for the Knapsack of weight 'weight'
			store[weight] = max(store[weight], store[weight-w[i]]+w[i])
	#Finding the value for the knapsack Weight
	return 	store[W]

input = sys.stdin.read()
W, n, *w = list(map(int, input.split()))
print(optimal_weight(W, w))
