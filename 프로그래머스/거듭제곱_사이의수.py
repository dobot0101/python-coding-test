from itertools import combinations

def solution(n):
    arr = []
    for i in range(n):
        if i == 0:
            arr.append(1)
        else:
            arr.append(3 ** i)
            
    arr_max = max(arr)
    
    temp_arr = []
    for i in range(2, len(arr) + 1):
        temp_arr += [sum(j) for j in list(combinations(arr, i)) if sum(j) < arr_max]
        
    
    return sorted(list(set(arr + temp_arr)))[n - 1]
