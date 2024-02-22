def quick(arr):
    if len(arr) <= 1:
        return arr
    pevot = arr[len(arr)//2]
    right = [x for x in arr if x < pevot]
    left = [x for x in arr if x >= pevot]

    return quick(right) + [pevot] + quick(left)
lis = [9,5,2,5,4,8,1,0]
print(quick(lis))