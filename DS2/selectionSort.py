def SS(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

def SSDecanting(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index] < arr[j]:
                min_index = j
            arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

def SSAoud(arr):
    ret = []
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
            arr[min_index], arr[i] = arr[i], arr[min_index]
    for i in arr:
        if i % 2 != 0:
            ret.append(i)
    return ret

def SSEven(arr):
    ret = []
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
            arr[min_index], arr[i] = arr[i], arr[min_index]
    for i in arr:
        if i % 2 == 0:
            ret.append(i)
    return ret


ar = [1,2,56,8,23,654,3,0]
print(SS(ar))
print(SSDecanting(ar))
print(SSAoud(ar))
print(SSEven(ar))


def selectionSort(arr):
    for i in range(len(arr)):
        sel = i
        for j in range(i,len(arr)):
            if arr[sel] > arr[j]:
                sel = j
        arr[sel], arr[i] = arr[i], arr[sel]
    return arr
print(selectionSort(ar))
