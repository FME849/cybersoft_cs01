lst_number = [18, 9, 4, 4, 2, 15, 16, 19, 27, 44, 50, 15, 15]

# Ex 1: Viết hàm tìm ra số lớn nhất trong list

def find_max(lst: list[int]):
    # output: max_number
    max_number:int = lst[0];

    #process
    for n in lst:
        if n > max_number:
            max_number = n
    return max_number

print(find_max(lst_number))