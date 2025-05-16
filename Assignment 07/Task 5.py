import heapq

N, M = map(int, input().split())

u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))

g = []
for _ in range(N + 1):
    g.append([])
for i in range(M):
    g[u[i]].append((v[i], w[i]))

dst = []
for _ in range(N + 1):
    dst.append([float('inf'), float('inf')])

dst[1][0] = 0
dst[1][1] = 0

priority_q = [(0, 1, 0), (0, 1, 1)]

while priority_q:
    cost, u, last = heapq.heappop(priority_q)
    if dst[u][last] < cost:
        continue

    for v, w in g[u]:
        new = w % 2
        if new != last:
            if dst[v][new] > cost + w:
                dst[v][new] = cost + w
                heapq.heappush(priority_q, (dst[v][new], v, new))

out = min(dst[N])
print(out if out != float('inf') else -1)
