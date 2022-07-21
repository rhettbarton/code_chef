T = int(input())
 
for a in range(T):
	N = int(input())
	array = raw_input().split()
	numTrue = 0
 
	for i in range(N):
		numTrue += int(array[i])
		
	numFalse = N - numTrue
	
	if numTrue%2 == 0:
		print numFalse
	else:
		print numTrue