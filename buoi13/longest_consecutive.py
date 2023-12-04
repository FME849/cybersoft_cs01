lst_num = [100, 4, 200, 1, 3, 2, 9, 10, 15, 14, 13, 12, 11]

def longest_consecutive(lst:list[int]):
    longest_set = 0
    set_lst = set(lst_num)
    for num in set_lst:
        if num - 1 not in set_lst:
            current_num = num
            current_set = 1

            while current_num + 1 in set_lst:
                current_set += 1
                current_num += 1

            longest_set = max(longest_set, current_set)
    
    return longest_set
        

print(longest_consecutive(lst_num))