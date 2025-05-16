N = int(input())
n_lst = list(map(int, input().split()))
M = int(input())
m_lst = list(map(int, input().split()))

merged = []

n_ind = 0
m_ind = 0
for i in range(M + N):
    if n_ind == N and m_ind < M:
        merged.extend(m_lst[m_ind:])
        break
    elif m_ind == M and n_ind < N:
        merged.extend(n_lst[n_ind:])
        break
    elif n_lst[n_ind] <= m_lst[m_ind]:
        merged.append(n_lst[n_ind])
        n_ind += 1
    else:
        merged.append(m_lst[m_ind])
        m_ind += 1

print(' '.join(map(str, merged)))