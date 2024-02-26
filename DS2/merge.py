# def merge_sort(array):
#     if len(array) <= 1:
#         return array

#     # Divide the array into two halves.
#     mid = len(array) // 2
#     left = merge_sort(array[:mid])
#     right = merge_sort(array[mid:])

#     # Merge the two sorted halves.
#     return merge(left, right)


# def merge(left, right):
#     result = []
#     i, j = 0, 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     # Add any remaining elements from the left or right subarray.
#     result += left[i:]
#     result += right[j:]

#     return result


# array = [5, 3, 2, 1, 4]

# sorted_array = merge_sort(array)

# print(sorted_array)


# def merge(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr)//2
#     lef = merge(arr[:mid])
#     rgt = merge(arr[mid:])

#     return mrg_sort(lef, rgt)
# def mrg_sort(lef,rgt):
#     res = []
#     l,r = 0,0
#     while l < len(lef) and r < len(rgt):
#         if lef[l] < rgt[r]:
#             res.append(lef[l])
#             l += 1
#         else:
#             res.append(rgt[r])
#             r += 1
#     res += lef[l:]
#     res += rgt[r:]
#     return res

# lis = [9,5,2,3,4,6,7,8,1,0]
# res = merge(lis)
# print(res)



def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    lef = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(lef, right)
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
lis = [9,5,2,3,4,6,7,8,1,0]
res = merge_sort(lis)
print(res)