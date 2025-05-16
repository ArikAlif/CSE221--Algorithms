N = int(input())
A = list(map(int, input().split()))

def binary_tree(arr, s, e, lst):
    if s > e:
        return
    mid = (s+e)//2
    lst.append(arr[mid])
    binary_tree(arr, s, mid-1, lst)
    binary_tree(arr, mid+1, e, lst)
    return lst

new_lst = binary_tree(A, 0, N-1, [])

print(' '.join(map(str, new_lst)))