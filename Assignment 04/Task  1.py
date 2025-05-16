s = input()
N, M = map(int, s.split())
lst = []
for i in range(N):
    r = [0]*N
    lst.append(r)

for i in range(M):
    st = input()
    n1, n2, w = map(int, st.split())
    lst[n1-1][n2-1] = w

for i in lst:
    print(' '.join(map(str, i)))
