person_count = int(input())
time_list = []
for _ in range(person_count):
  time_list.append(int(input()))

# time_list = [10, 20, 30, 40, 50, 60, 70]
# time_list = [1, 2, 5, 10]

time_list.sort()

crossed_time_list = []
result = time_list[1]
crossed_time_list.append(time_list.pop(0))
crossed_time_list.append(time_list.pop(0))

crossed_time_list.sort()
result += crossed_time_list[0]
time_list.append(crossed_time_list.pop(0))
print(time_list)
print(crossed_time_list)

while len(time_list) > 0:
  # 큰 값부터 다리 건넘
  time_list = sorted(time_list, reverse = True)
  print(time_list)
  # time_list.sort(reverse = True)
  result += time_list[0]
  crossed_time_list.append(time_list.pop(0))
  crossed_time_list.append(time_list.pop(0))
  
  # 건넌 값 중 최소값 다시 건넘
  if len(time_list) > 0:
    crossed_time_list.sort()
    result += crossed_time_list[0]
    time_list.append(crossed_time_list.pop(0))

print(result)
