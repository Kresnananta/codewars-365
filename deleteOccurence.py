def delete_nth(order,max_e):
    counts = {}
    i = 0
    while i < len(order):
        num = order[i]
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > max_e:
            order.pop(i)
            counts[num] -= 1  
        else:
            i += 1
        
    return order

# 6 kyu
# print(delete_nth([1,2,3,1,2,3,1,2,3],2))