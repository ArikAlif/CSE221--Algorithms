N = int(input())
g = []
for i in range(N-1):
    a,b = map(int,input().split())
    g.append((a,b))

def diameter(N, g):
    adj_lst = []
    for _ in range(N+1):
        adj_lst.append([])

    for u, v in g:
        adj_lst[u].append(v)
        adj_lst[v].append(u)

    def BFS(root):
        distance = [-1] * (N + 1)
        queue = [0] * N
        next = 0
        prev = 0
        queue[prev] = root
        prev += 1
        distance[root] = 0
        max = root

        while next < prev:
            u = queue[next]
            next += 1
            for v in adj_lst[u]:
                if distance[v] == -1:
                    distance[v] = distance[u] + 1
                    queue[prev] = v
                    prev += 1
                    if distance[v] > distance[max]:
                        max = v
        return max, distance[max]

    a, _ = BFS(1)
    b, d = BFS(a)
    print(d)
    print(a, b)

diameter(N, g)
