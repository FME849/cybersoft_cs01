lst_number = [18, 9, 4, 4, 2, 15, 16, 19, 27, 44, 50, 15, 15]

# Ex 1: Viết hàm tìm ra số lớn nhất trong list

def find_max(lst: list):
    # input: lst: list
    
    # output: max_number
    max_number = 0;

    #process
    for n in lst:
        if n > max_number:
            max_number = n
    print(max_number)

find_max(lst_number)