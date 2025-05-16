N, M = map(int, input().split())
g = []
for _ in range(M):
    u, v, w = map(int, input().split())
    g.append((w, u, v))

g.sort()

par = [i for i in range(N+1)]
count = [1] * (N + 1)

def find(x):
    if par[x] == x:
        return par[x]
    return (find(par[x]))
    
def union(u, v):
    u_parent = find(u)
    v_parent = find(v)

    if u_parent != v_parent:
        if count[u_parent] < count[v_parent]:
            u_parent, v_parent = v_parent, u_parent
        par[v_parent] = u_parent
        count[u_parent] += count[v_parent]

        return True
    else:
        return False

tree = [[] for _ in range(N + 1)]
mst_cost = 0
used = [False] * M 

for i in range(N):
    w, u, v = g[i]
    if union(u, v):
        mst_cost += w
        tree[u].append((v, w))
        tree[v].append((u, w))
        used[i] = True


def dfs(u, p, target, max_w):
    if u == target: 
        return max_w
    for v, w in tree[u]:
        if v != p:
            out = dfs(v, u, target, max(max_w, w))
            if out != -1: 
                return out
    return -1

second = float('inf')
for i in range(M):
    if not used[i]:
        w, u, v = g[i]
        max_on_path = dfs(u, -1, v, 0)
        if max_on_path != -1 and w > max_on_path:
            second = min(second, mst_cost - max_on_path + w)


if second != float('inf'):
    print(second)
else:
     print( -1)
