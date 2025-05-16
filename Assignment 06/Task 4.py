N, R = map(int, input().split())
g = []
for i in range(N - 1):
    a, b = map(int, input().split())
    g.append((a, b))
Q = int(input())
count = []
for i in range(Q):
    count.append(int(input()))


def tree_query(N, R, g, count):
    adj_lst = []
    for i in range(N+1):
        adj_lst.append([])

    for u, v in g:
        adj_lst[u].append(v)
        adj_lst[v].append(u)

    size = [0]*(N+1)
    visited = [False]*(N+1)
    parent = [0]*(N+1)

    stack = [0]*(2*N)
    head = 0
    order = []
    stack[head] = R
    head += 1

    while head > 0:
        current = stack[head-1]
        head -= 1
        if not visited[current]:
            visited[current] = True
            order.append(current)
            for neighbor in adj_lst[current]:
                if not visited[neighbor]:
                    stack[head] = neighbor
                    head += 1
                    parent[neighbor] = current


    for i in range(len(order)-1, -1, -1):
        i = order[i]
        size[i] = 1
        for neighbor in adj_lst[i]:
            if neighbor != parent[i]:
                size[i] += size[neighbor]

    for j in count:
        print(size[j])


tree_query(N, R, g, count)
