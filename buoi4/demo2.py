# Viết chương trình nhập vào số dòng và số cột in ra ma trận sao tương ứng
# Vd: so_dong = 3 và so_cot = 5
#   * * * * *
#   * * * * *
#   * * * * *

#input: so_dong:int, so_cot:int
so_dong:int = int(input("Please input row number: "))
so_cot:int = int(input("Please input column number: "))

#output: matrix:str
matrix:str = ''

#process
column_th = so_cot
while so_dong > 0:
    while column_th > 0:
        matrix += '* '        
        column_th -= 1
        
    matrix += '\n'
    column_th = so_cot
    so_dong -= 1
    
print(matrix)