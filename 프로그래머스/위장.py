def solution(clothes):
    d = {}
    for clothe in clothes:
      key = clothe[1]
      value = clothe[0]

      if key in d:
        d[key].append(value)
      else:
        d[key] = [value]

    answer = 1
    for key in d.keys():
      answer *= (len(d[key]) + 1)

    return answer - 1


solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])