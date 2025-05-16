s = input()
N, M = map(int, s.split())

start = list(map(int, input().split()))
end = list(map(int, input().split()))
lst = [0]*N
for i in range(M):
    lst[start[i]-1] += 1
    lst[end[i]-1] += 1

count = 0

for i in lst:
    if i % 2 != 0:
        count += 1
    
if count == 0 or count ==2:
    print('YES')
else:
    print('NO')