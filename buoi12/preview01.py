lst_number:list[int] = [20,81,97,63,72,11,20,15,33,15,41,20]

def sum_total(lst:list[int]):
    result:int = 0
    # for n in lst:
    #     result += n

    for index,num in enumerate(lst):
        result += num
    return result

print(f"Total of list:", sum_total(lst_number))