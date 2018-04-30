# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0
max_index1, max_index2 = -1, -1

for i in range(n):
	if max_index1 == -1 or a[i] > a[max_index1]:
		max_index1 = i

for i in range(n):
	if i!=max_index1 and (max_index2 == -1 or a[i] > a[max_index2]):
		max_index2 = i

print(a[max_index1]*a[max_index2])