N, K = map(int, input().split())

g = [i for i in range(N+1)]
count = [1] * (N+1)

def find(x):
    if g[x] == x:
        return g[x]
    return (find(g[x]))
    
def friends(u, v):
    u_parent = find(u)
    v_parent = find(v)

    if u_parent != v_parent:
        if count[u_parent] < count[v_parent]:
            u_parent, v_parent = v_parent, u_parent
        g[v_parent] = u_parent
        count[u_parent] += count[v_parent]

    return count[find(u)]

for _ in range(K):
    u, v = map(int, input().split())
    print(friends(u, v))