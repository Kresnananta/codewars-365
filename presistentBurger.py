def persistence(n):
    num = str(n)
    temp = 1
    count = 0
    while len(num) != 1:
        for i in num:
            temp *= int(i)
        num = str(temp)
        temp = 1
        count += 1
        
    return count

# 6 kyu
# print(persistence(39))