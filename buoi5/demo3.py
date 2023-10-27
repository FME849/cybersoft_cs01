# Viết chương trình cho phép người dùng nhập vào 1 chuỗi bất kỳ và nhập vào 1 ký tự, kiểm tra ký tự đó có trong chuỗi hay không. Nếu có trả về vị trí tìm thấy, nếu không trả về vị trí -1

#input input:str, char:str
text:str = input("Please input a text: ")
char:str = input("Please input a char: ")

#output idx:int
idx:int = -1

#process
# current_idx:int = 0
# while idx < 0 and current_idx < len(text):
#     if char == text[current_idx]:
#         idx = current_idx

#     current_idx += 1
    
for i in range(0, len(text)):
    if char == text[i]:
        idx = i
        break

print(idx)