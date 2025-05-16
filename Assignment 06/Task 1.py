N, M = map(int, input().split())
g = []
for i in range(M):
    a, b = map(int, input().split())
    g.append((a, b))

def advising(N, g):
    adj = []
    for i in range(N + 1):
        adj.append([])
    indeg = [0] * (N + 1)

    for a, b in g:
        adj[a].append(b)
        indeg[b] += 1

    queue = [0] * (N + 1)
    next = 0
    prev = 0

    for i in range(1, N + 1):
        if indeg[i] == 0:
            queue[prev] = i
            prev += 1

    out = []
    while next < prev:
        current = queue[next]
        next += 1
        out.append(current)
        for neighbor in adj[current]:
            indeg[neighbor] -= 1
            if indeg[neighbor] == 0:
                queue[prev] = neighbor
                prev += 1 

    if len(out) == N:
        print(' '.join(map(str, out)))
    else:
        print(-1)

advising(N, g)
