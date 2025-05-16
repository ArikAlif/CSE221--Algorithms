T = int(input())
for i in range(T):
    S = input()
    L = len(S)
    left = 0
    right = L-1
    mid = (left+right)//2
    if S[0]=='1':
        print(1)
        continue
    if '1' not in S:
        print(-1)
        continue
    while left <= right:
        mid = (right+left)//2
        if S[mid] == '1' and S[mid-1]=='0':
            print(mid+1)
            break
        elif S[mid] == '0':
            left = mid + 1
        elif S[mid] == '1' and S[mid-1] != '0':
            right = mid - 1