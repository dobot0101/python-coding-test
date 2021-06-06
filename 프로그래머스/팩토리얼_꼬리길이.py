def solution(n):
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count
    
    # num = factorial(n)
    
    # while num % 10 == 0:
    #     count += 1
    #     num /= 10
    # return count
        
        
    # for i in range(len(num)-1, -1, -1):
    #     if num[i] == '0':
    #         count += 1
    #     else:
    #         break
    # return count

# def factorial(n):
#     if n == 1 or n == 2:
#         return 1
#     return n * factorial(n - 1)