#input: 1 số int do người dùng nhập vào
nhiet_do:int = int(input("Nhập vào nhiệt độ: "))

#output: 
output:str = ""

#process:
if nhiet_do < 25:
    output = "Không mở điều hoà!"
else:
    output = "Mở điều hoà!"

print(output)