# Viết chương trình cho phép người dùng nhập vào 1 chuỗi và số lần xuất hiện của chuỗi đó, in ra màn hình kết quả tương ứng

#input: so_lan:int, text:str
so_lan:int = int(input("Nhập vào số lần lặp: "))
text:str = input("Nhập vào chuỗi muốn lặp: ")

#output: ket_qua:str
ket_qua:str = ''

#process
while so_lan > 0:
    if so_lan == 1:
        ket_qua += text
    else:
        ket_qua += (text + '\n')
    
    so_lan -= 1

print(ket_qua)