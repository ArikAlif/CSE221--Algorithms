N, M = map(int, input().split())
g = []
for i in range(M):
    a, b = map(int, input().split())
    g.append((a, b))

def match(N, g):
    adj_lst = []
    for i in range(N+1):
        adj_lst.append([])
    for u, v in g:
        adj_lst[u].append(v)
        adj_lst[v].append(u)

    visited_check = [-1]*(N+1)
    max_size = 0

    queue = [0]*(N+1)

    for i in range(1, N + 1):
        if visited_check[i] == -1:
            next = 0
            prev = 0
            queue[prev] = i
            prev += 1
            visited_check[i] = 0
            count = [1, 0]
            while next < prev:
                u = queue[next]
                next += 1
                for j in adj_lst[u]:
                    if visited_check[j] == -1:
                        visited_check[j] = 1 - visited_check[u]
                        count[visited_check[j]] += 1
                        queue[prev] = j
                        prev += 1
                    elif visited_check[j] == visited_check[u]:
                        return -1

            max_size += max(count[0], count[1])

    print(max_size)

match(N, g)
