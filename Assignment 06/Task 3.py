s = int(input())
x1, y1, x2, y2 = map(int, input().split())

def knight_of_konigsberg(s, x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        print(0)
        return

    x_coords = [-2, -1, 1, 2, 2, 1, -1, -2]
    y_coords = [1, 2, 2, 1, -1, -2, -2, -1]

    size = (s+1)*(s+1)

    visited = [False]*size
    distance = [-1]*size

    def idx(x, y):
        return x*(s+1)+y

    queue = [(0, 0)]*size
    front = 0
    rear = 0
    queue[rear] = (x1, y1)
    rear += 1

    visited[idx(x1, y1)] = True
    distance[idx(x1, y1)] = 0

    while front < rear:
        x, y = queue[front]
        front += 1

        for i in range(8):
            nx = x + x_coords[i]
            ny = y + y_coords[i]
            if 1 <= nx <= s and 1 <= ny <= s and not visited[idx(nx, ny)]:
                visited[idx(nx, ny)] = True
                distance[idx(nx, ny)] = distance[idx(x, y)] + 1
                if nx == x2 and ny == y2:
                    print(distance[idx(nx, ny)])
                    return
                queue[rear] = (nx, ny)
                rear += 1

    print(-1)

knight_of_konigsberg(s, x1, y1, x2, y2)
