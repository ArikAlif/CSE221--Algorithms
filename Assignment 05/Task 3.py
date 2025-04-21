N, M, S, D = map(int, input().split())

adj_lst = []

e1 = list(map(int, input().split()))
e2 = list(map(int, input().split()))

for i in range(N+1):
    adj_lst.append([])

for i in range(M):
    adj_lst[e1[i]].append(e2[i])
    adj_lst[e2[i]].append(e1[i])

for i in adj_lst:
    i.sort()

def BFS(N, S, D, lst):

    dist = [-1]*(N+1)
    visited = [False]*(N+1)
    prev = [-1]*(N+1)
    queue = []
    queue.append(S)
    head = 0
    visited[S] = True
    dist[S] = 0


    while head<len(queue):
        v = queue[head]
        head+=1
        for next in lst[v]:
            if visited[next] == False:
                visited[next] = True
                dist[next] = dist[v]+1
                prev[next] = v
                queue.append(next)

    if visited[D]==False:
        return -1, []

    shortest_path = []
    current_pos = D
    while current_pos != -1:
        shortest_path.append(current_pos)
        current_pos = prev[current_pos]

    shortest_path.reverse()

    return dist[D], shortest_path

dst, path = BFS(N, S, D, adj_lst)

if dst == -1:
    print(-1)
else:
    print(dst)
    print(' '.join(map(str, path)))
            