# Viết chương trình cho phép người dùng nhập vào rows và cols in ra ma trận sao tương ứng
import method
#input rows:int, cols:int
rows:int = int(input('Please input rows: '))
cols:int = int(input('Please input cols: '))

#output: matrix:str
matrix:str = ''

#process
for i in range(0, rows):
    matrix += method.print_stars(cols)
    matrix += '\n'

print(matrix)