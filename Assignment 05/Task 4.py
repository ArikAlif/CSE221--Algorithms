N, M, S, D, K = map(int, input().split())

adj_lst = []

for i in range(N+1):
    adj_lst.append([])

for j in range(M):
    a, b = map(int, input().split())
    adj_lst[a].append(b)

def BFS(N, S, D, lst):

    dst = [-1]*(N+1)
    visited = [False]*(N+1)
    prev = [-1]*(N+1)
    queue = [S]
    head = 0
    visited[S] = True
    dst[S] = 0

    while head<len(queue):
        current = queue[head]
        head+=1
        for next in lst[current]:
            if visited[next]==False:
                visited[next] = True
                dst[next] = dst[current]+1
                prev[next] = current
                queue.append(next)

    if dst[D] == -1:
        return -1, []
    
    path = []
    position = D

    while position != -1:
        path.append(position)
        position = prev[position]
    path.reverse()

    return dst[D], path

s2k, path1 = BFS(N, S, K, adj_lst)
k2d, path2 = BFS(N, K, D, adj_lst)

if s2k == -1 or k2d == -1:
    print(-1)

else:
    total_dst = path1 + path2[1:]
    print(len(total_dst)-1)
    print(' '.join(map(str, total_dst)))

    