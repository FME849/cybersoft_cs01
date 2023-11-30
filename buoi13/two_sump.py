lst_number = [2, 7, 11, 15, 99, 70, 100, 20, 35, 60]

def two_sump(lst:list[int], target:int):
    dict_int = {}

    for idx, number in enumerate(lst):
        remain = target - number
        if remain in dict_int:
            return [dict_int[remain], idx]
        dict_int[number] = idx
    return None

print(two_sump(lst_number, 120))