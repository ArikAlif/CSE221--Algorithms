N, M = map(int, input().split())

adj_lst = []

for i in range(N+1):
    adj_lst.append([])

for j in range(M):
    a, b = map(int, input().split())
    adj_lst[a].append(b)

visited = [0]*(N+1)
cycle = False

for s in range(1, N+1):
    if visited[s] == 0:
        stack = [(s,0)]
        path = []

        while stack:
            current, ind = stack[-1]
            if visited[current] == 0:
                visited[current] = 1
                path.append(current)

            next = adj_lst[current]
            if ind<len(next):
                next = next[ind]
                stack[-1] = (current, ind+1)

                if visited[next] == 0:
                    stack.append((next, 0))
                elif visited[next] == 1:
                    cycle = True
                    break
            else:
                visited[current] = 2
                stack.pop()
                path.pop()

    if cycle: 
        break

if cycle == True:
    print('YES')
else:
    print('NO')