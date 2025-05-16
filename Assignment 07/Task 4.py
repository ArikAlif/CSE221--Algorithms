import heapq

N, M, S, D = map(int, input().split())
w = list(map(int, input().split()))
w = [0] + w 

g = []
for _ in range(N + 1):
    g.append([])

for _ in range(M):
    u, v = map(int, input().split())
    g[u].append(v)

cost = [float('inf')] * (N + 1)
cost[S] = w[S]
priority_q = [(cost[S], S)]

while priority_q:
    current_cost, u = heapq.heappop(priority_q)
    if current_cost > cost[u]:
        continue
    for v in g[u]:
        new_cost = current_cost + w[v]
        if new_cost < cost[v]:
            cost[v] = new_cost
            heapq.heappush(priority_q, (new_cost, v))


print(cost[D] if cost[D] != float('inf') else -1)
