# Viết chương trình nhập vào 1 số, in ra số đó có phải là số nguyên tố hay không

#input: n:int
n:int = int(input("Nhập vào số n: "))

#output: ket_qua:str
ket_qua:str = ''

#process
so_uoc:int = 0
so_chia:int = 1

while so_chia <= n:
    if n % so_chia == 0:
        so_uoc += 1

    so_chia += 1

if so_uoc == 2:
    ket_qua = f"{n} là số nguyên tố"
else:
    ket_qua = f"{n} không là số nguyên tố"

print(ket_qua)
