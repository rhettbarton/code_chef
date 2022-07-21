AB = raw_input().split()
A = int(AB[0])
B = int(AB[1])

diff = A - B
diff = list(str(diff))
L = len(diff)
diff[L-1] = str(abs(int(diff[L-1]) - 1))
diff = int(''.join(diff))

if diff == 0:
  diff = 2

print diff