def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def BSDecanting(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def BSAoudNum(arr):
    ret = []
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    for k in arr:
        if k % 2 != 0:
            ret.append(k)
    return ret

def BSEvenNum(arr):
    ret = []
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    for k in arr:
        if k % 2 == 0:
            ret.append(k)
    return ret



ar = [1,4,3,8,2,6,0]
print(bubbleSort(ar))
print(BSDecanting(ar))
print(BSAoudNum(ar))
print(BSEvenNum(ar))