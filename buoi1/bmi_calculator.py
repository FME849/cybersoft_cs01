# B1: Nhập cân nặng và chiều cao từ người dùng
weight:int = int(input("Nhập cân nặng: "))
height:float = float(input("Nhập chiều cao: "))

# B2: Xác định biến kết quả
bmi_index:float = 0.0

# B3: process
bmi_index = weight / (height ** 2)
print("Chỉ số BMI:", bmi_index)