import heapq
N, M, S, T = map(int, input().split())

g = []
for _ in range(N + 1):
    g.append([])

for _ in range(M):
    u, v, w = map(int, input().split())
    g[u].append((v,w))


def two_point(N, start, g):
    dst = [float('inf')] * (N + 1)
    dst[start] = 0
    priority = [(0, start)]

    while priority:
        d, u = heapq.heappop(priority)
        if d > dst[u]:
            continue
        for v, w in g[u]:
            if dst[v] > d + w:
                dst[v] = d + w
                heapq.heappush(priority, (dst[v], v))
    return dst


S_dst = two_point(N, S, g)
T_dst = two_point(N, T, g)

min_time = float('inf')
meeting_node = -1

for i in range(1, N + 1):
    if S_dst[i] != float('inf') and T_dst[i] != float('inf'):
        max_time = max(S_dst[i], T_dst[i])
        if max_time < min_time or (max_time == min_time and i < meeting_node):
            min_time = max_time
            meeting_node = i

if meeting_node == -1:
    print(-1)
else:
    print(min_time, meeting_node)
