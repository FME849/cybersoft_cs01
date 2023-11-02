#input n:int
n:int = int(input("Please input a number: "))

#output isosceles_triangle:str
isosceles_triangle:str = ''

#process
for i in range(1, n + 1):
    space = (n - i) * '  '
    star = (2 * i - 1) * '* '
    isosceles_triangle += space + star + space + '\n'

print(isosceles_triangle)