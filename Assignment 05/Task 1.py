N, M = map(int, input().split())
adj_lst = []

for i in range(N+1):
    adj_lst.append([])

for edges in range(M):
    a, b = map(int, input().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)

def BFS(N, lst):
    visited = [False]*(N+1)
    out = []
    queue = []

    queue.append(1)
    visited[1] = True

    while queue:
        v = queue.pop(0)
        out.append(v)
        for i in lst[v]:
            if visited[i]==False:
                visited[i] = True
                queue.append(i)

    return out


result = BFS(N, adj_lst)

print(' '.join(map(str, result)))
