#input text:str
text:str = input("Please input a string: ")

#output output:str
output:str = ''

#process
# for i in range(len(text) - 1, -1, -1):
#     output += text[i]
    
for char in text:
    output = char + output

print(output)