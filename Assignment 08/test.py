import heapq
N, M = map(int,input().split())
g =[]
for i in range(M):
    u, v, w = map(int,input().split())
    g.append((w, v, u))
g.sort()

par = [i for i in range(N+1)]
count = [1] * (N+1)

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
total = 0
for i in g:
    if union(i[1], i[2]):
        total += i[0]

print(total)