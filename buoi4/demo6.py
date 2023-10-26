# Sử dụng vòng lặp while để in ra tất cả các ký tự trên chuỗi

text:str = "Hello World!"
output:str = ''
for i in range(0, len(text)):
    output += text[i] + '\n'

print(output)