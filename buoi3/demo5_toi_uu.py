# Viết chương trình nhập vào 1 số, in ra số đó có phải là số nguyên tố hay không

import math
#input: n:int
n:int = int(input("Nhập vào số n: "))

#output: ket_qua:str
ket_qua:str = ''

#process
flag:bool = True
so_chia:int = 2

if n <= 1:
    flag = False

while so_chia <= math.sqrt(n):
    if n % so_chia == 0:
        flag = False

    so_chia += 1

if flag:
    ket_qua = f"{n} là số nguyên tố"
else:
    ket_qua = f"{n} không là số nguyên tố"

print(ket_qua)
