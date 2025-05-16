N = int(input())

lst = []
for i in range(N):
    r = [0]*N
    lst.append(r)

for i in range(N):
    s = list(map(int, input().split()))
    for j in range(s[0]):
        lst[i][s[j+1]] = 1

for i in lst:
    print(' '.join(map(str, i)))
