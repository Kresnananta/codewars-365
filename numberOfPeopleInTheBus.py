def high(x):
    x = x.split()
    alphaDict = {}
    res = []
    for i in range(26):
        l = chr(ord('a') + i)
        alphaDict[l] = i + 1

    for i in x:
        score = sum(alphaDict[char] for char in i)
        res.append(score)
    
    max_index = res.index(max(res))
    return x[max_index]

# 6 kyu
# print(high('man i need a taxi up to ubud')) 