def ISAssenting(arr):
    for i in range(1,len(arr)):
        current = arr[i]
        j = i - 1

        while arr[j] > current and j >= 0:
            arr[j+1] = arr[j]
            j-=1
        
        arr[j+1] = current
    return arr

def ISDecanting(arr):
    for i in range(1,len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and current > arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current
    return arr

def ISAoud(arr):
    for i in range(1,len(arr)):
        current = arr[i]
        j = i - 1
        while j >=0 and current < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current
    ret = []
    for i in arr:
        if i % 2 != 0:
            ret.append(i)
    return ret

def ISEven(arr):
    for i in range(1,len(arr)):
        current = arr[i]
        j = i - 1
        while j >=0 and current < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = current
    ret = []
    for i in arr:
        if i % 2 == 0:
            ret.append(i)
    return ret



ar = [1,4,6,8,6,42,4,5,2,10]
print(ISAssenting(ar))
print(ISDecanting(ar))
print(ISAoud(ar))
print(ISEven(ar))


def insertion(arr):
    for i in range(len(arr)):
        cu = arr[i]
        j = i - 1
        while j > 0 and cu < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = cu
    return arr
print(insertion(ar))
