def two_sum(lst:list[int], target:int):
    result:list[int] = []
    for idx,num in enumerate(lst):
        if num <= target:
            for i in range(idx, len(lst) - idx):
                if num + lst[i] == target:
                    result = [idx, i]
        
    return result

print(two_sum([2, 7, 11, 15], 9))