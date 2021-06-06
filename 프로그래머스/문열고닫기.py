


# 소수 목록 구하기
def get_sosu(n):
    sieve = [True] * (n+1)

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           
            for j in range(i+i, n+1, i): 
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n+1) if sieve[i] == True]


def solution(n):
    # sosu_list = get_sosu(n)
    # print(sosu_list)
    door_state = {i: True for i in range(1, n+1)}
    door_state_keys = door_state.keys()
    
    for i in range(2, n+1):
        if i > n / 2:
            door_state[i] = not door_state[i]
        else:
            for key in door_state_keys:
                if key % i == 0:
                    door_state[key] = not door_state[key]
        print(door_state)

        
    # sorted_door_state = dict(sorted(door_state.items(), key=lambda x:x[1], reverse=True))
    # return len([value for value in sorted_door_state.values() if value == True])
    
    # door_state_list = list(door_state.values())
    # door_state_list.sort(reverse=True)
    # return door_state_list.count(True)

    # return list(door_state.values()).count(True)
    return len([value for value in door_state.values() if value == True])

solution(5)