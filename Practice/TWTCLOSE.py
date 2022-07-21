NK = raw_input().split()
N = int(NK[0])
K = int(NK[1])
clicks = ['']*K
op = [0]*N

for i in range(K):
  clicks[i] = raw_input()
  if clicks[i] == 'CLOSEALL':
    op = [0]*N
  else:
    num = clicks[i].split()
    if op[int(num[1])-1] == 1:
      op[int(num[1])-1] = 0
    else:
      op[int(num[1])-1] = 1
  print sum(op)