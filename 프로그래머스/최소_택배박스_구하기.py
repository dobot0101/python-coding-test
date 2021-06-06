
# 박스 꽉 채운 경우에만 박스 수 return
# 어떤 경우에도 박스를 가득 채우지 못하면 -1 return
def solution(n):
    count = 0
    box_size_list = [5, 3]
    
    for box_size in box_size_list:
        count += n // box_size
        n %= box_size
        
    if n != 0:
        return -1
    
    return count

print(solution(17))
