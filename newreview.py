def fact(n):
    if n == 1:
        return 1
    else: 
        return n * fact(n-1)
print(fact(5))



def febi(n):
    if n <= 1:
        return n
    else:
        return febi(n-1) + febi(n-2)

for i in range(10):
    print(febi(i))

def selection(arr):
    for i in range(len(arr)):
        sel = i
        for j in range(i, len(arr)):
            if arr[j] < arr[sel]:
                sel = j
        arr[i], arr[sel] = arr[sel], arr[i]
    return arr

arrr = [10,20,3,1,6,43,100,8]
print("Selection sort :",selection(arrr))

def insertion(arr):
    for i in range(1,len(arr)):
        j = i-1
        sel = arr[i]
        while j >= 0 and sel < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = sel
    return arr
print("insertion sort : ",insertion(arrr))

def bubble(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr
print("bubble sort : ",bubble(arrr))

def quick(arr):
    if len(arr) <= 1:
        return arr
    pv = arr[len(arr)//2]
    gt = [x for x in arr if x > pv]
    lt = [x for x in arr if x < pv]
    eq = [x for x in arr if x == pv]
    return quick(lt) + eq + quick(gt)
print("Quick sort : ", quick(arrr))

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)
def merge(right,left):
    rearr = []
    l, r = 0,0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            rearr.append(left[l])
            l+=1
        else:
            rearr.append(right[r])
            r+=1
    rearr += left[l:]
    rearr += right[r:]
    return rearr
print("merge sort : ", mergeSort(arrr))
