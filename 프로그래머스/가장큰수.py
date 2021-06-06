
def solution(numbers):
  a = list(map(str, numbers))
  a.sort(key = lambda x: x * 3, reverse = True)
  return str(int(''.join(a)))

    # temp_arr = []
    # for i in numbers:
    #     temp = str(i)
    #     print(temp)
    #     for j in numbers:
    #         if i == j:
    #             continue
    #         temp += str(j)
    #         print(temp)
    #     temp_arr.append(temp)
    
    # return max(temp_arr)

print(solution([6, 10, 2]))