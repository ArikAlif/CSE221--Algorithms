n, q = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(q):
    l, h = map(int, input().split())
    count = 0
    for j in range(n):
        if l<=arr[j]<=h:
            count += 1
    print(count)

n, q = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(q):
    l, h = map(int, input().split())
    l_ind = 0
    h_ind = 0
    # left = 0
    # right = n-1
    # while left <= right:
    #     if arr[left]< l:
    #         l_ind += 1
    #     if arr[right] > h:
    #         h_ind -= 1
    #     left = left+1
    #     right = right-1
    #     break
    for j in range(n):
        if arr[j] >= l:
            l_ind = j
            break
    for k in range(n-1,-1,-1):
        if arr[k] <= h:
            h_ind = k
            break
    print(h_ind - l_ind +1)