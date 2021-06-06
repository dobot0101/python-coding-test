def solution(s1, s2):
    s3 = delete_duplicate(s1, s2)
    s4 = delete_duplicate(s2, s1)

    if len(s3) > len(s4):
      return s4
    elif len(s3) == len(s4):
      return s3 if s4 > s3 else s4
    else:
      return s3

# 중복 문자열 제거 함수
def delete_duplicate(s1, s2):
    new_str = s1
    for i in range(1, len(s2)+1):
        if new_str[-i:] == s2[:i]:
            new_str = new_str[:-i]
            break
    new_str += s2
    return new_str

print(solution("xyZA", "ABCxy"))