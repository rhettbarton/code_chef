def second_largest(numbers):
    count = 0
    m1 = m2 = int(1)
    for x in numbers:
        count += 1
        if x > m2:
            if x >= m1:
                m1, m2 = x, m1            
            else:
                m2 = x
    return m2 if count >= 2 else None

T = int(raw_input())

for a in range(T):
	n = int(raw_input())
	L = raw_input().split()
	R = raw_input().split()
	LR = [0]*n

	# if n == 1:
	# 	print 1
	# 	continue

	for i in range(n):
		L[i] = int(L[i])
		R[i] = int(R[i])	
		LR[i] = L[i]*R[i]

	maxLR = max(LR)
	max2LR = second_largest(LR)

	if maxLR != max2LR:
		print LR.index(maxLR) + 1
		continue

	for i in range(n):
		if LR[i] != maxLR:
			R[i] = 0

	maxR = max(R)

	print R.index(maxR) + 1