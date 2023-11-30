lst_nums = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 4, 4, 4, 5, 5]

def find_most(lst:list[int]):
    num_hash = {}
    for i in lst:
        if i in num_hash:
            num_hash[i] += 1
        else:
            num_hash[i] = 1
    return max(num_hash.values())

print(find_most(lst_nums))