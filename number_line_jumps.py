
# 캥거루 2마리가 뛴다
# 캥거루의 시작 위치는 각각 x1, x2 (항상 x1 < x2)
# 캥거루의 점프 길이는 각각 v1, v2
# 두 캥거루가 같은 위치에서 만날 수 있으면 'YES' 아니면 'NO' return

def kangaroo(x1, v1, x2, v2):
    while True:
      if v1 <= v2: 
        return 'NO'
      else:
        x1 += v1
        x2 += v2

        if x1 == x2: 
          return 'YES'
          
        if x1 > x2: 
          return 'NO'


print(kangaroo(4523, 8092, 9419, 8076))