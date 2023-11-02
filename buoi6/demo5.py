import method
#input
n:int = int(input("Please input a number: "))

#output 
output:str = ''

#process
if n < 2:
    output = 'There is no prime number'
else:
    for i in range(2, n + 1):
        if method.is_prime_number(i):
            output += f"{i} "

print(output)