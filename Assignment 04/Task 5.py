s = input()
N, M = map(int, s.split())

start = list(map(int, input().split()))
end = list(map(int, input().split()))
lst = [0]*N
for i in range(M):
    lst[start[i]-1] -= 1
    lst[end[i]-1] += 1


print(' '.join(map(str, lst)))

