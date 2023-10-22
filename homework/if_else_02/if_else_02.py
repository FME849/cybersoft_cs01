#input weight:float, distance:float
weight:float = float(input("Please input your weight of product: "))
distance:float = float(input("Please input your distance: "))

#output: bill:float
bill:float = 0.0

#process
if weight < 3:
    bill = weight * 20000
else:
    bill = weight * 30000

if distance < 10:
    bill = bill + distance * 20000
else:
    bill = bill + distance * 30000

print("Your delivery bill is:", bill)