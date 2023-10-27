# Cho 1 chuỗi số, tìm vị trí số lớn nhất trong chuỗi
# Vd: "749325"

#input
input = "749325"

#output
idx:int = 0

#process
max:int = 0
for i in range(0, len(input)):
    current_number = int(input[i])
    if  current_number > max:
        max = current_number
        idx = i
    
print(idx)