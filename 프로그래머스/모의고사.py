
# 너무 어렵게 푼 것 같다.
def solution(answers):
    dict = {}
    dict[0] = [1,2,3,4,5]
    dict[1] = [2,1,2,3,2,4,2,5]
    dict[2] = [3,3,1,1,2,2,4,4,5,5]
    
    result = {i:0 for i in range(3)}
    for i in range(3):
        for j in range(len(answers)):
            if answers[j] == dict[i][j % len(dict[i])]:
                result[i] += 1
    
    
    sorted_result = sorted(result.items(), key=lambda x:(-x[1], x[0]))
    max_num = max([value for key, value in sorted_result])
    max_list = [key + 1 for key, value in sorted_result if value == max_num]
    
    return max_list

print(solution([1,2,3,4,5]))