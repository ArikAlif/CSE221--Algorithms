first = input()
l, t = first.split()
l = int(l)
t = int(t)
arr = input()
arr = arr.split()
for i in range(l):
    arr[i] = int(arr[i])

def finder(arr, l):
    left = 0
    right = l-1
    while True:
        if left == right:
            return -1
        elif arr[left] + arr[right] == t:
            return f'{left+1} {right+1}'
        elif arr[left] + arr[right] < t:
            left += 1
        elif arr[left] + arr[right] > t:
            right -= 1

print(finder(arr,l))