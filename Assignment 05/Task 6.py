R, H = map(int, input().split())
grid = []
for i in range(R):
    r = input().strip()
    grid.append(r)

visited = []
for i in range(R):
    r = []
    for j in range(H):
        r.append(False)
    visited.append(r)

coordinates = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def BFS(X,Y):
    queue = [(X, Y)]
    visited[X][Y] = True

    if grid[X][Y] == 'D':
        diamonds = 1
    else:
        diamonds = 0
    head = 0

    while head < len(queue):
        a, b = queue[head]
        head += 1
        for c_a, c_b in coordinates:
            n_a, n_b = a + c_a, b + c_b
            if 0 <= n_a < R and 0 <= n_b < H:
                if visited[n_a][n_b]==False and grid[n_a][n_b] != '#':
                    visited[n_a][n_b] = True
                    queue.append((n_a, n_b))
                    if grid[n_a][n_b] == 'D':
                        diamonds += 1
    return diamonds

max_diamonds = 0
for i in range(R):
    for j in range(H):
        if visited[i][j]==False and grid[i][j] != '#':
            max_diamonds = max(max_diamonds, BFS(i, j))

print(max_diamonds)
