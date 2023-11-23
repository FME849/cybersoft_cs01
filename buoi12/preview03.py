lst_number = [1, 1, 2, 2, 2, 3, 4, 4, 5]

def remove_duplicate(lst:list[int]):
    current_num = lst[0]
    output = [current_num]
    for i in lst:
        if i > current_num:
            output.append(i)
            current_num = i
    
    return output

print(remove_duplicate(lst_number))