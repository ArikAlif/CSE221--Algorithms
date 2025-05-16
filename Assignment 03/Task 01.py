def merge(a, b):
    global inv_count
    new = []
    a_ind = 0
    b_ind = 0
    while a_ind<len(a) and b_ind<len(b):
        if a[a_ind]<b[b_ind]:
            new.append(a[a_ind])
            a_ind += 1
        else:
            new.append(b[b_ind])
            b_ind += 1
            inv_count += len(a)-a_ind

    new.extend(a[a_ind:])
    new.extend(b[b_ind:])
    
    return new
    
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])   
        a2 = mergeSort(arr[mid:])  
        return merge(a1, a2)       

N = int(input())     
A = list(map(int, input().split()))
inv_count = 0
new_arr = mergeSort(A)
print(inv_count)
new = ' '.join(map(str, new_arr))
print(new)