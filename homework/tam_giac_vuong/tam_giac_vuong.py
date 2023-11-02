#input n:int
n:int = int(input("Please input a number: "))

#output right_triangle:str
right_triangle:str = ''

#process
for i in range(1, n + 1):
    j = 1
    while j < n + 1:
        if j > i:
            right_triangle += '  '
        else:
            right_triangle += '*  '
        
        j += 1
    
    right_triangle += '\n'

print(right_triangle)