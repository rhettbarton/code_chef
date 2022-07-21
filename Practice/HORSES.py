T = int(input())
 
for x in range(T):
  N = int(input())
  S = raw_input().split()
  S = map(int,S)
  S.sort()
 
  min_diff = abs(S[0] - S[1])
  
  for i in range(1,len(S)):
    if min_diff == 0:
      break
    diff = abs(S[i] - S[i-1])
    if diff < min_diff:
      min_diff = diff

  print min_diff