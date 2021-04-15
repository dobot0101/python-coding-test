# 점수가 38점 미만이면 반올림 X
# 점수가 38점 이상이고, 
# 다음 5의 배수와의 차가 3 미만이면 5의 배수 return, 
# 다음 5의 배수와의 3 이상이면 점수 그대로 return
# return 값 배열 print

def gradingStudents(grades):
    result = []
    for grade in grades:
        if grade < 38:
            result.append(grade)
            continue
            
        i = grade
        while i % 5 != 0:
            i += 1
        
        if (i - grade) < 3:
            result.append(i)
        else:
            result.append(grade)
            
    return result


list = [4,73,67,38,33]

result = gradingStudents(list)

print(result)