# linked list

class node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class linkedList:
    def __init__(self):
        self.head = None
    
    def add_node(self,data):
        newNode = node(data)
        if self.head is None:
            self.head = newNode
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = newNode
    
    def printData(self):
        if self.head is None:
            print("linked list is empty")
        else:
            t = self.head
            while t is not None:
                print(t.data)
                t = t.ref

# new = linkedList()
# new.printData()
# new.add_node(10)
# new.add_node(20)
# new.add_node(30)
# new.printData()


# insertion sort
arr = [1,34,6,4,19,86,7,234,3]
for i in range(len(arr)):
    cur = arr[i]
    j = i-1
    while j >= 0 and cur < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = cur
print(arr)


# selection sort
arr2 = [1,34,6,4,19,86,7,234,3]
for i in range(len(arr2)):
    mi = i
    for j in range(i,len(arr2)):
        if arr2[mi] > arr2[j]:
            mi = j
        arr2[i], arr2[mi] = arr2[mi], arr2[i]
print(arr2)

# bubble sort

arr = [1,34,6,4,19,86,7,234,3]
for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)


# quick sort

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    
    pev = arr[len(arr)//2]
    gr = [x for x in arr if x < pev]
    eq = [x for x in arr if x == pev]
    ls = [x for x in arr if x > pev]

    return quickSort(gr) + eq + quickSort(ls)
arrr = [4,19,86,7,234,1,3]
print(quickSort(arrr))


# merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    l_ar = arr[:mid]
    r_ar = arr[mid:]
    la = merge_sort(l_ar)
    ra = merge_sort(r_ar)
    return merge(la,ra)
    
def merge(left, right):
    res = []
    l, r = 0, 0
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
    
arrr = [4,19,86,7,234,1,3]
print(merge_sort(arrr))