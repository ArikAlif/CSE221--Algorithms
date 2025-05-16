s = input()
N, M = map(int, s.split())

e1 = list(map(int, input().split()))
e2 = list(map(int, input().split()))
w = list(map(int, input().split()))

adj_lst = []

for i in range(N):
    adj_lst.append([])

for i in range(M):
    adj_lst[e1[i]-1].append((e2[i],w[i]))

for i in range(N):
    print(f'{i+1}:',end='')
    for j in range(len(adj_lst[i])):
        if j == len(adj_lst[i])-1:
            print(adj_lst[i][j], end='')
        else:
            print(adj_lst[i][j], end=' ')
    print()