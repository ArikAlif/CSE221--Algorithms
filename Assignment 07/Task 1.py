import heapq

N, M, S, D = map(int, input().split())

u_lst = []
v_lst = []
w_lst = []

for i in range(3):
    x = list(map(int, input().split()))
    if i ==0:
        u_lst = x
    elif i == 1:
        v_lst = x
    else:
        w_lst = x



def shortest_path(N, M, S, D, u, v, w):

    g = []
    for _ in range(N + 1):
        g.append([])

    for i in range(M):
        g[u[i]].append((v[i], w[i]))

    dist = []
    prev = []
    visited = []
    for _ in range(N + 1):
        dist.append(float('inf'))
        prev.append(-1)
        visited.append(False)

    dist[S] = 0
    priority = []
    heapq.heappush(priority, (0, S))

    while priority:
        head = heapq.heappop(priority)
        current_dist = head[0]
        u = head[1]

        if visited[u]:
            continue
        visited[u] = True

        for i in range(len(g[u])):
            v, w = g[u][i]
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(priority, (dist[v], v))

    if dist[D] == float('inf'):
        print(-1)
    else:
        print(dist[D])
        path = []
        curr = D
        while curr != -1:
            path.append(curr)
            curr = prev[curr]
        i = len(path) - 1
        while i >= 0:
            print(path[i], end=' ')
            i -= 1
        print()

shortest_path(N, M, S, D, u_lst, v_lst, w_lst)