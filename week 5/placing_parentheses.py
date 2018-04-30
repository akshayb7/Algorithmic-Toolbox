# Uses python3
def evalt(a, b, op):
	if op == '+':
		return a + b
	elif op == '-':
		return a - b
	elif op == '*':
		return a * b
	else:
		assert False

def Min_and_Max(i,j,op,m,M):
	minimum = 10000000
	maximum = -10000000
	for k in range(i,j):
		a = evalt(M[i][k], M[k+1][j], op[k])
		b = evalt(M[i][k], m[k+1][j], op[k])
		c = evalt(m[i][k], M[k+1][j], op[k])
		d = evalt(m[i][k], m[k+1][j], op[k])
		minimum = min(minimum,a,b,c,d)
		maximum = max(maximum,a,b,c,d)
	return (minimum,maximum)	
				
def get_maximum_value(dataset):
	op = dataset[1:len(dataset):2]
	d = dataset[0:len(dataset)+1:2]
	n = len(d)
	m = [[0 for i in range(n)] for j in range(n)]
	M = [[0 for i in range(n)] for j in range(n)]
	for i in range(n):
		m[i][i] = int(d[i])
		M[i][i] = int(d[i])
	for i in range(1,n):
		for j in range(n-i):
			k = i+j
			m[j][k],M[j][k] = Min_and_Max(j,k,op,m,M)
	return M[0][n-1]		

print(get_maximum_value(input()))
