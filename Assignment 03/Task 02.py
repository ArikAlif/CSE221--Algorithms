N = int(input())
A = list(map(int, input().split()))
A = list(map(abs, A))
mid = len(A)//2
 
def find_largest(arr):
    if len(arr) == 1:
        return arr[0], float('-inf'), 0
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[0], arr[1], 0
        else:
            return arr[1], arr[0], 1
    
    mid = len(arr)//2
    left1, left2, left_ind = find_largest(arr[:mid])
    right1, right2, right_ind = find_largest(arr[mid:])
 
    if left1 > right1:
        largest = left1
        second = max(left2, right1)
        largest_ind = left_ind
        if left2 > right1:
            second_ind = arr.index(left2)
        else:
            second_ind = arr.index(right1)
 
    else:
        largest = right1
        second = max(right2, left1)
        largest_ind = right_ind
        if right2 > left1:
            second_ind = arr.index(right2)
        else:
            second_ind = arr.index(left1)
 
    return largest, second, largest_ind
 
left1, left2 , left_ind= find_largest(A[:mid])
right1, right2, right_ind = find_largest(A[mid:])
 
new = []
max1 = (right1**2)+left1
new.append(max1)
if left_ind > A.index(left2):
    max2 = (left1 ** 2) + left2
    new.append(max2)

if right_ind > A.index(right2):
    max3 = (right1 ** 2) + right2
    new.append(max3)

print(max(new))