import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

T = int(input())

for a in range(T):
	lin = raw_input()
	lin = lin.split()
	n = int(lin[0])
	m = int(lin[1])

	table = [[0 for j in range(m)] for i in range(n)]

	for i in range(n):
		lin = raw_input()
		for j in range(m):
			table[i][j] = int(lin[j])

	sum = [0]*m
	for j in range(m):
		for i in range(n):
			sum[j] += table[i][j]

	coll = 0 
	for j in range(m):
		if sum[j] > 1:
			coll += nCr(sum[j],2)

	print coll