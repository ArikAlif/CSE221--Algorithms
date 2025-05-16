N, v = map(int, input().split())
adj_lst = []

for i in range(N):
    adj_lst.append([])

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
for i in range(1, N+1):
    for j in range(1, 1+N):
        if gcd(i,j)==1 and i!=j:
            adj_lst[i-1].append(j)
    adj_lst[i-1].sort()



ver_pos = []
for i in range(v):
    a, b = map(int, input().split())
    ver_pos.append((a,b))
for a,b in ver_pos:
    if b>len(adj_lst[a-1]):
        print(-1)
    else:
        print(adj_lst[a-1][b-1])

