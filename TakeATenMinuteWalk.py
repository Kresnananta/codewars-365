def is_valid_walk(walk):
    coor = [0,0]
    count = 0
    for i in walk:
        match i:
            case 'n':
                coor[0] += 1
            case 's':
                coor[0] += -1
            case 'e':
                coor[1] += 1
            case 'w':
                coor[1] += -1
                
        count += 1
    
    if coor == [0,0] and count == 10:
        return True
    else:
        return False
    
# 6 kyu
# print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))