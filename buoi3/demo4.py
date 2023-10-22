#input n:int
n:int = int(input("Nhập vào số n: "))

#output tong_2n:int
tong_2n:int = 0

#process
while n > 0:
    tong_2n += (2 * n)
    n -= 1

print(tong_2n)