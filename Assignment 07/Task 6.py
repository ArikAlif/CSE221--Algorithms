import heapq

N, M, S, D = map(int, input().split())

g = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    g[u].append((v, w))
    g[v].append((u, w)) 

dst = [[float('inf'), float('inf')] for _ in range(N + 1)]
dst[S][0] = 0

priority_q = [(0, S)] 
while priority_q:
    cost, u = heapq.heappop(priority_q)
    
    for v, w in g[u]:
        new = cost + w
        if new < dst[v][0]:
            dst[v][1] = dst[v][0]
            dst[v][0] = new
            heapq.heappush(priority_q, (new, v))
        elif dst[v][0] < new < dst[v][1]:
            dst[v][1] = new
            heapq.heappush(priority_q, (new, v))

out = dst[D][1]
print(out if out != float('inf') else -1)
