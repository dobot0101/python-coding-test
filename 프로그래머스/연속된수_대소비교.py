def solution(estimates, k):
    estimates.sort()
    answer = 0
    print(estimates)
    for _ in range(k):
        i = estimates.pop()
        print(i)
        answer += i
    
    return answer

solution([10, 1, 10, 1, 1, 4, 3, 10], 6)