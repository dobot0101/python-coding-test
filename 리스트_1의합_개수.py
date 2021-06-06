from itertools import combinations

def solution(U, L, C):
    upper_arr = [0 for _ in range(len(C))]
    lower_arr = [0 for _ in range(len(C))]
    idx_arr = []
    for i in range(len(C)):
        if C[i] == 2:
            upper_arr[i] = 1
            lower_arr[i] = 1
        elif C[i] == 0:
            upper_arr[i] = 0
            lower_arr[i] = 0
        elif C[i] == 1:
            idx_arr.append(i)
            upper_arr[i] = 1
            lower_arr[i] = 0


    if validate_possible(upper_arr, lower_arr, U, L):
        return make_result_str(upper_arr, lower_arr)
    else:
        # upper_arr와 lower_arr의 1을 바꿔가며 각 arr의 1개수 확인
        for i in range(1, len(idx_arr) + 1):
            for j in list(combinations(idx_arr, i)):
                for k in j:
                    temp = upper_arr[k]
                    upper_arr[k] = lower_arr[k]
                    lower_arr[k] = temp
                if validate_possible(upper_arr, lower_arr, U, L):
                    return make_result_str(upper_arr, lower_arr)

        return 'IMPOSSIBLE'

# 결과 문자열 생성
def make_result_str(upper_arr, lower_arr):
    return ''.join(map(str, upper_arr)) + ',' + ''.join(map(str, lower_arr))

# upper_arr, lower_arr 1 개수 확인
def validate_possible(upper_arr, lower_arr, U, L):
    if upper_arr.count(1) == U and lower_arr.count(1) == L:
        return True
    else:
        return False

print(solution(3, 2, [2, 1, 1, 0, 1]))