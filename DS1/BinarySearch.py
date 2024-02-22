def binary_search():
    values = []
    n = int(input("Length of list : "))
    for i in range(n):
        values.append(int(input(f'value {i+1} : ')))
    print("-----------------")
    while True:
        search = int(input("search key :"))
        low=0
        high=len(values)-1
        while low<=high:
            mid=low+high//2
            if values[mid] == search:
                print(search,"element found at position",mid+1)
                break
            elif search <= values[mid]:
                high = mid 
            else:
                low = mid
        else:
            print("Element not found")

binary_search()