# def quickSort(arr):
#     if len(arr) <= 1:
#         return arr
#     pev = arr[len(arr)//2]
#     les = [x for x in arr if x < pev]
#     eql = [x for x in arr if x == pev]
#     grt = [x for x in arr if x > pev]

#     return quickSort(les) + eql + quickSort(grt)
# lis = [9,5,2,5,4,8,1,0]
# pp = quickSort(lis)
# print(pp)

def Quick(arr):
    if len(arr) <= 1:
        return arr
    pev = arr[len(arr)//2]
    les = [x for x in arr if x < pev]
    grt = [x for x in arr if x > pev]
    eql = [x for x in arr if x == pev]
    return Quick(les) + eql + Quick(grt)

lis = [9,5,2,3,4,6,7,8,1,0]
res = Quick(lis)
print(res)