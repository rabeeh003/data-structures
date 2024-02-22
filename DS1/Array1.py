def find_max(arr):
    maxItem = arr[0]

    for i in arr:
        if i > maxItem:
            maxItem = i

    return maxItem

def find_min(arr):
    minItem = arr[0]

    for i in arr:
        if i < minItem:
            minItem = i

    return minItem

def remove_duplicates(arr):
    re_array = []
    
    for i in arr:
        if i not in re_array:
            re_array.append(i)

    return re_array
    
def find_sum(arr):
    sum = 0

    for i in arr:
        sum = sum + i
    
    return sum

array = [1,3,5,6,2,4,7,8,9,4,3,2,1,5,6,8,9]

maxItem = find_max(array)
print("Maximum number is",maxItem)

minItem = find_min(array)
print("Minimum number is",minItem)

sumNumber = find_sum(array)
print("Sum of all numbers is",sumNumber)

duplicate_removed = remove_duplicates(array)
print(duplicate_removed)