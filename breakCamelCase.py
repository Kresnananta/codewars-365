def solution(s):
    check_up = []
    sentence = []
    for i in range(len(s)):
        if s[i].isupper():
            check_up.append(i)
    
    first = 0
    for i in check_up:
        sentence.append(s[first:i])
        first = i
    sentence.append(s[first:len(s)])
    
    return ' '.join(sentence)

# 6 kyu
# print(solution('breakCamelCase'))