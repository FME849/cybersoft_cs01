# Sử dụng for để viết chương trình nhập vào 1 số nguyên n, in ra số sao tương ứng

#input n:int
n = int(input("Please input a number: "))

#output result:str
result:str = ''

#process
for i in range(1, n + 1):
    result += '* '

print(result)
