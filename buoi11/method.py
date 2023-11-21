def find_max(lst: list[int]):
    # output: max_number
    max_number:int = lst[0];

    #process
    for n in lst:
        if n > max_number:
            max_number = n
    return max_number