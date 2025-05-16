user = input()
S, K = user.split()
S = int(S)
K = int(K)
N = input()
N = N.split()
R = N[(K-S-1)::-1]
for i in range(len(R)):
    print(R[i], end=' ')
