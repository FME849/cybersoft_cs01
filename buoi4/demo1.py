# Viết chương trình cho phép người dùng nhập vào 1 số nguyên n => và in ra số * tương ứng

#input n:int
n:int = int(input("Please input a number: "))

#output result:str
result:str = ''

#process
while n > 0:
    result = result + '* '
    n -= 1

print(result)