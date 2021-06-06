def solution(arr, n):
    dict = {i:0 for i in arr if i <= n}
    print(dict)

    for key in dict.keys():
      if n - key in dict:
        return True

    return False

print(solution([100000000, 99999998, 1, 9, 13], 100000000))
print(solution([5, 3, 9, 13], 7))