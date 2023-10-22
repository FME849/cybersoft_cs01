#input: number:int
number:int = int(input("Please input a number: "))

#output: result:str
result:str = ""

#process
if number % 2 == 0:
    result = "This number is even"
else: 
    result = "This number is odd"

print(result)