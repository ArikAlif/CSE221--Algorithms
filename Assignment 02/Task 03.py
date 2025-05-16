s = input()
N, K = s.split()
N, K = int(N), int(K)
arr = list(map(int, input().split()))

count = 0
for i in range(N):
    sum = 0
    tmp_count = 0
    if count < N-i:
        for j in range(i,N):
            sum += arr[j]
            if sum <= K:
                tmp_count += 1
            else:
                break
        count = max(count, tmp_count)
    else:
        break

print(count)