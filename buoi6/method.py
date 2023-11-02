import math

def display(day:int, month:int, year = 2000):
    """
        Mô tả hàm: Hàm này nhận vào input là các số nguyên ứng với ngày tháng năm. Thực hiện chức năng để in ra ngày tháng năm
            input:
                day: ngày
                month: tháng
                year: năm
    """
    print("Day:", str(day))
    print("Month:", str(month))
    print("Year:", str(year))

def print_stars(n:int):
    output = ''

    #process
    for i in range(0, n):
        output += '* '
    
    return output

def matrix_stars(rows:int, cols:int):
    output = ''

    for i in range(0, rows):
        output += print_stars(cols) + '\n'
    
    return output

def calculate_average_score(toan:float, ly:float, hoa:float):
    """
    Hàm tính điểm trung bình dựa vào 3 tham số điểm toán, lý, hoá
        Input:
            toan (float): 1 -> 10
            ly (float): 1 -> 10
            hoa (float): 1 -> 10
        Output:
            dtb (float): điểm trung bình 3 môn toán, lý, hoá
    """
    output:float = 0
    output = (toan + ly + hoa) / 3
    return output

def classify(score:float):
    """
    Hàm này sẽ nhận vào giá trị dtb là 1 số thực (float). Và xử lý trả ra xếp loại Giỏi,Khá,Trung Bình, Yếu dựa theo 1 số quy tắt 
        input: là 1 số thực ví dụ 6.7
            dtb (float): Số thực
            
        output: là string xếp loại ví dụ Khá
            xepLoai (string):  
    """
    output:str = ''

    if score < 5:
        output = "Yeu"
    elif 5 <= score < 6.5:
        output = "TB"
    elif 6.5 <= score < 8:
        output = "Kha"
    elif 8 <= score <= 10:
        output = "Gioi"

    return output

def is_prime_number(n:int):
    output:bool = True
    divide_number = 2
    if n < 2:
        output = False
        return output
    
    while divide_number <= math.sqrt(n) and output:
        if n % divide_number == 0:
            output = False
        divide_number += 1
    
    return output

