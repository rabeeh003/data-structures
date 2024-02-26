print("------- Sorting methods -------")
print("-------------------------------")

# ----------------------------------------
# insertion sort :

# arr = [8,5,3,1,3,8,4,9]
# for i in range(len(arr)):
#     j = i - 1
#     sel = arr[i]
#     while j >= 0 and arr[j+1] < arr[j]:
#         arr[j+1], arr[j] = arr[j], arr[j+1]
#         j -= 1
#     arr[j+1] = sel

# print("Insertion sort : ",arr)


def insertion(arr):
    for i in range(len(arr)):
        cur = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > cur:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = cur
    return arr
arr = [8,5,3,1,3,8,4,9]
print("Insertion sort : ",insertion(arr))

# ----------------------------------------
# # selection sort

# arr = [8,5,3,1,3,8,4,9]
# for i in range(len(arr)):
#     sel = i
#     for j in range(i,len(arr)):
#         if arr[sel] > arr[j]:
#             sel = j
#     arr[i], arr[sel] = arr[sel], arr[i]
# print(arr)


arr = [1,7,4,2,9,0,3,1,6]
for i in range(len(arr)):
    sel = i
    for j in range(i,len(arr)):
        if arr[sel] > arr[j]:
            sel = j
    arr[i], arr[sel] = arr[sel], arr[i]
print("Selection sort :",arr)

# --------------------------------------------------
# Bubble sort

arr = [1,7,3,2,7,90,7,43,7,0]
for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print("Bubble sort : ",arr)


# arr = [8,5,3,1,3,8,4,9]
# for i in range(len(arr)):
#     for j in range(0,len(arr)-i-1):
#         if arr[j+1] < arr[j]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
# print(arr)


# --------------------------------------------------
# insertion sort

# arr = [10,23,42,63,12,3,75,3,1,0]
# for i in range(len(arr)):
#     j = i - 1
#     sel = arr[i]
#     while j >= 0 and arr[j] > arr[j+1]:
#         arr[j+1], arr[j] = arr[j], arr[j+1]
#         j -= 1
#     arr[j+1] = sel
# print(arr)


# --------------------------------------------------
# Quick sort


# def quickSort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     priv = arr[len(arr) // 2]
#     less = [x for x in arr if x < priv]
#     equal = [x for x in arr if x == priv]
#     grat = [x for x in arr if x > priv]
#
#     return quickSort(less) + equal + quickSort(grat)
# ar = [20,39,1,4,74,5]
# qu = quickSort(ar)
# print(qu)



# def quick(arr):
#     if len(arr) <= 1:
#         return arr
#     pevot = arr[len(arr)//2]
#     less = [x for x in arr if x < pevot]
#     equal = [x for x in arr if x == pevot]
#     grater = [x for x in arr if x > pevot]
#     return quick(less) + equal + quick(grater)
# lis = [9,5,2,5,4,8,1,0]
# print(quick(lis))



# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     less = []
#     grat = []
#     pivot = arr.pop()
#     for i in arr:
#         if i < pivot:
#             less.append(i)
#         else:
#             grat.append(i)
#     return quick_sort(less) + pivot + quick_sort(grat)
# arr = [7,4,6,4,3,2,9,0]
# p = quick_sort(arr)
# print(p)



# def quick(arr):
#     if len(arr) <= 1:
#         return arr
#     priv = arr[len(arr)//2]
#     less = [x for x in arr if x < priv]
#     equal = [x for x in arr if x == priv]
#     grater = [x for x in arr if x > priv]
#     return quick(less) + equal + quick(grater)
#
# pp = quick([19,7,5,3,23,45,6,0])
# print(pp)


# def quick(arr):
#     if len(arr) <= 1:
#         return arr
#     priv = arr.pop()
#     less = []
#     grat = []
#     for i in arr:
#         if i < priv:
#             less.append(i)
#         else:
#             grat.append(i)
#     return quick(less) + [priv] + quick(grat)
# ar = [65,23,4,1,8]
# p = quick(ar)
# print(p)


def quick(arr):
    if len(arr) <= 1:
        return arr

    pev = arr[len(arr)//2]
    les = [x for x in arr if x < pev]
    eql = [x for x in arr if x == pev]
    grt = [x for x in arr if x > pev]

    return quick(les) + eql + quick(grt)
arr = [75,687,24,2,5,3,1]
print("Quick sort : ",quick(arr))

# --------------------------------------
# merge sort

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     half = len(arr)//2
#     l_arr = arr[:half]
#     r_arr = arr[half:]
#
#     lh = merge_sort(l_arr)
#     rh = merge_sort(r_arr)
#
#     return merge(lh, rh)
#
# def merge(left,right):
#     res = []
#     l, r = 0, 0
#
#     while l < len(left) and r < len(right):
#         if left[l] <= right[r]:
#             res.append(left[l])
#             l += 1
#         else:
#             res.append(right[r])
#             r += 1
#
#     res.extend(left[l:])
#     res.extend(right[r:])
#
#     return res
#
# arr = [38, 27, 43, 3, 9, 82, 10]
# sorted_arr = merge_sort(arr)
# print("Sorted array:", sorted_arr)




def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    l_arr = arr[:mid]
    r_arr = arr[mid:]
    la = merge_sort(l_arr)
    ra = merge_sort(r_arr)
    return merge(la,ra)
def merge(left,right):
    res = []
    l,r = 0,0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    res.extend(left[l:])
    res.extend(right[r:])
    return res
arr = [87,56,34,65,24,97,20,1]
sa = merge_sort(arr)
print("Merge sort : ",sa)