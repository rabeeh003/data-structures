def merge_sort(array):
    if len(array) <= 1:
        return array

    # Divide the array into two halves.
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    # Merge the two sorted halves.
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements from the left or right subarray.
    result += left[i:]
    result += right[j:]

    return result


array = [5, 3, 2, 1, 4]

sorted_array = merge_sort(array)

print(sorted_array)