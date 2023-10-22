# Viết chương trình cho phép người dùng nhập vào 1 số n, tính tổng từ 1 đến n và in ra màn hình

#input n:int
n:int = int(input("Nhập vào số n: "))

#output ket_qua:int
ket_qua = 0

#process
while n > 0:
    ket_qua += n
    n -= 1

print(ket_qua)