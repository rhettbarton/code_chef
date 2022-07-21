nm = input().split()
N = int(nm[0])
M = int(nm[1])

spec = input().split()
for i in range(len(spec)):
	spec[i] = int(spec[i])

unorderedList = [[0 for j in range(3)] for i in range(M)]

for i in range(M):
	line = input().split()
	for j in range(3):	
		if j == 2:
			unorderedList[i][j] = line[j]
		else:
			unorderedList[i][j] = int(line[j])
	if unorderedList[i][0] in spec:
		unorderedList[i][0] = 1
	else:
		unorderedList[i][0] = 2

orderedList = sorted(unorderedList, key=lambda tup: tup[1], reverse = True)
orderedList = sorted(orderedList, key=lambda tup: tup[0])

for i in range(M):
	print(orderedList[i][2])

    