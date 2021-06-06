# a = [1,2,3,4]
# b = {key:item for key,item in enumerate(a)}
# b = {i:0 for i in a}
# print(b)

# a = {i:1 for i in range(3)}
# print(a.items())
# # a.sort(key=lambda x:x[1])
# sorted_a = sorted(a.items(), key=lambda x:(-x[1], x[0]))
# print(sorted_a)

# sorted_a = sorted(a.items(), key=lambda x:(-x[0], x[1]))
# print(sorted_a)
# for i in range(len(a)):
#   print(i, a[i])
# a = 5
# print(1 % 3)

# # 푸는 중...
# def solution(N, coffee_times):
#     order_list = [i+1 for i in range(len(coffee_times))]

#     temp_arr = [coffee_times[0],coffee_times[1],coffee_times[2]]
#     while len(temp_arr) > 0:
#       for i in range(N):
#         temp_arr[i] -= temp_arr[i]
#         if temp_arr[i] == 0:
#           temp_arr.pop(i)

#     print(temp_arr)
    


# print(solution(3, [4, 2, 2, 5, 3]))
# # # # result: [2, 3, 1, 5, 4]
