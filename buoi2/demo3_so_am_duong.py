# Viết chương trình nhập vào 1 số nguyên xuất ra kết quả số đó là số âm hay số dương

#input: n:int
n:int = int(input("Nhập vào 1 số nguyên: "))

#output: ket_qua:str
ket_qua:str = ""

#process
if n < 0:
    output = "Số âm"
else:
    output = "Số dương"

print(output)