import math


def radix_sort(lists, radix=10):
    if max(lists) % radix == 0:
        k = int(math.ceil(math.log(max(lists), radix))) + 1
    else:
        k = int(math.ceil(math.log(max(lists), radix)))
    bucket = [[] for i in range(radix)]
    for i in range(1, k+1):
        for j in lists:
            bucket[j//(radix**(i-1)) % radix].append(j)
        del lists[:]
        for z in bucket:
            lists += z
            del z[:]
    print(lists)
    return lists

radix_sort([13,31,24,56,74,56,89,47,100])