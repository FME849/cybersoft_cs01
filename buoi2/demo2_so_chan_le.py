# Viết chương trình nhập vào 1 số nguyên xuất ra kết quả số đó là số chẵn hay số lẻ

#input: n:int
n:int = int(input("Nhập vào 1 số nguyên: "))

#output: output:str
output:str = ""

#process
if n % 2 == 0:
    output = "Số chẵn"
else:
    output = "Số lẻ"

print(output)