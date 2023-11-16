#input: diem_toan, diem_ly, diem_hoa
diem_toan:float = float(input("Nhập vào điểm toán: "))
diem_ly: float = float(input("Nhập vào điểm lý: "))
diem_hoa: float = float(input("Nhập vào điểm hoá: "))

#output diem_trung_binh, xep_loai
diem_trung_binh: float = 0.0
xep_loai:str = ""

#process
diem_trung_binh = (diem_toan + diem_ly + diem_hoa) / 3
if diem_trung_binh > 9:
    xep_loai = "A"
elif 8 < diem_trung_binh <= 9:
    xep_loai = "B"
elif 7 < diem_trung_binh <= 8:
    xep_loai = "C"
elif 5 < diem_trung_binh <= 7:
    xep_loai = "D"
else:
    xep_loai = "F"

print(diem_trung_binh, xep_loai)