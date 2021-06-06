import collections
def groupSort(arr):
    arr.sort()
    
    counter = collections.Counter(arr)

    result = []
    for key, value in counter.items():
        result.append([key, value])

    result.sort(key = lambda x:(-x[1], x[0]))
    return result
