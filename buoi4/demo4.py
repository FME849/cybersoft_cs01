#input: so_dong:int, so_cot:int
so_dong:int = int(input("Please input row number: "))
so_cot:int = int(input("Please input column number: "))

#output: matrix:str
matrix:str = ''

#process
for row in range(0, so_dong):
    for column in range(0, so_cot):
        matrix += '* '        
        
    matrix += '\n'
    
print(matrix)