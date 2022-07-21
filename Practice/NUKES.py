ANK = raw_input().split()
A = int(ANK[0])
N = int(ANK[1])
K = int(ANK[2])
chambers = [0]*K
explode = [0]*K
num = A
results = ''

for i in range(K):
  explode[i] = int(num/(N+1))
  chambers[i] = num%(N+1)
  num = explode[i]

for j in range(K):
  results += str(chambers[j])
  if j < K-1:
    results += " "
    
print results