#input: 
# nhập lương cơ bản: luong_co_ban:int
luong_co_ban:int = int(input("Nhập lương cơ bản 1h: "))
# nhập số giờ làm: gio_lam:int
gio_lam:int = int(input("Nhập số giờ làm: "))


#output: tien_luong:int
tien_luong = 0

#process
gio_tang_ca = gio_lam - 40
if gio_tang_ca > 0:
    tien_luong = 40 * luong_co_ban + (gio_tang_ca * luong_co_ban * 1.5)
else:
    tien_luong = gio_lam * luong_co_ban

print("Tiền lương:",tien_luong)