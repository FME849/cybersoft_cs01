def find_max(lst: list[int]):
    # output: max_number
    max_number:int = lst[0];

    #process
    for n in lst:
        if n > max_number:
            max_number = n
    return max_number

def find_indexes(lst: list[int]):
    # input: user_input:int
    user_input:int = int(input("Please input a number: "))

    # output:
    output:list[int] = []

    # process
    for idx in range(0, len(lst)):
        if lst[idx] == user_input:
            output.append(idx)
    if len(output) > 0:
        return (f"Các vị trí chứa {user_input} là: {output}")
    else:
        return ("Không tìm thấy giá trị")
