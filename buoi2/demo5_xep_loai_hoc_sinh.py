""" 
Viết chương trình cho phép người dùng nhập vào điểm toán, điểm văn. 
Tính điểm trung bình và xếp loại theo công thức sau:
DTB < 5: Yếu
5 <= DTB < 6.5: Trung bình
6.5 <= DTB < 8: Khá
8 <= DTB <= 10: Giỏi
in ra điểm trung và xếp loại
"""

#input: diem_toan, diem_van
diem_toan:float = float(input("Nhập vào điểm toán: "))
diem_van: float = float(input("Nhập vào điểm văn: "))

#output
diem_trung_binh: float = 0.0
xep_loai:str = ""

#process
diem_trung_binh = (diem_toan + diem_van) / 2
if diem_trung_binh < 5:
    xep_loai = "Yếu"
elif 5 <= diem_trung_binh < 6.5:
    xep_loai = "Trung bình"
elif 6.5 <= diem_trung_binh < 8:
    xep_loai = "Khá"
else:
    xep_loai = "Giỏi"

print(diem_trung_binh, xep_loai)