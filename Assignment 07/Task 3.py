import heapq

N, M = map(int, input().split())

g = []
for _ in range(N + 1):
    g.append([])

for _ in range(M):
    u, v, w = map(int, input().split())
    g[u].append((v, w))
    g[v].append((u, w))


dngr = [float('inf')] * (N + 1)
dngr[1] = 0


prioroty = [(0, 1)]
while prioroty:
    dst, u = heapq.heappop(prioroty)
    if dst > dngr[u]:
        continue
    for v, w in g[u]:
        dngr2 = max(dst, w)
        if dngr2 < dngr[v]:
            dngr[v] = dngr2
            heapq.heappush(prioroty, (dngr2, v))


for i in range(1, N + 1):
    print(dngr[i] if dngr[i] != float('inf') else -1, end=' ')
print()
