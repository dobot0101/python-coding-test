def braces(values):
    open_braces = ['{', '(', '[']
    close_braces = ['}', ')', ']']
    
    result = []
    for i in range(len(values)):
        result.append('YES')
        
        stack = []
        for brace in values[i]:
            if brace in open_braces:
                stack.append(brace)
                continue

            if not stack:
                result[i] = 'NO'
                break

            open_brace = stack.pop()
            if brace != close_braces[open_braces.index(open_brace)]:
                result[i] = 'NO'
                break
        if stack:
            result[i] = 'NO'
            
    return result

print(braces(['{{}}', '{(()})']))
