#input: text:str
text:str = input("Please input a text: ")

#output: output:str
output:str = ''

#process
# reversed_text = ''
# for char in text:
#     reversed_text = char + reversed_text;

# if text == reversed_text:
#     output = 'Đây là chuỗi đối xứng'
# else:
#     output = 'Đây không phải là chuỗi đối xứng'

is_mirror:bool = True
for i in range(0, len(text) // 2):
    if text[i] != text[len(text) - 1 - i]:
        is_mirror = False
        break

if is_mirror:
    output = 'Đây là chuỗi đối xứng'
else:
    output = 'Đây không phải là chuỗi đối xứng'

print(output)