def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    right = mergesort(arr[mid:])
    left = mergesort(arr[:mid])

    return merge(left,right)

def merge(left, right):
    res = []
    l,r = 0,0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    res += left[l:]
    res += right[r:]
    return res
lis = [6,43,13,32,54,1]
print(mergesort(lis))