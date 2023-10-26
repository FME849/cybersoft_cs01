text:str = 'Hello World!'

output:str = ''
for i in range(len(text) - 1, -1, -1):
    output += text[i]

print(output)