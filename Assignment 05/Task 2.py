N, M = map(int, input().split())

e1 = list(map(int, input().split()))
e2 = list(map(int, input().split()))

adj_lst = []

for i in range(N+1):
    adj_lst.append([])

for i in range(M):
    adj_lst[e1[i]].append(e2[i])
    adj_lst[e2[i]].append(e1[i])

def DFS(lst, N):
    stack = [1]
    out = []
    visited = [False]*(N+1)

    while stack:
        a = stack.pop()
        if visited[a]==False:
            visited[a] = True
            out.append(a)
            for next in lst[a]:
                if visited[next] == False:
                    stack.append(next)

    
    return out

result = DFS(adj_lst, N)
print(' '.join(map(str, result)))
