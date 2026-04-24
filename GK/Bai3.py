def tinh_bmi(can_nang, chieu_cao):
    return can_nang / (chieu_cao ** 2)


def phan_loai(bmi):
    if bmi < 18.5:
        return "Gầy"
    elif bmi < 25:
        return "Bình thường"
    else:
        return "Thừa cân"


def nhap_so(thong_bao):
    while True:
        try:
            value = float(input(thong_bao))
            return value
        except ValueError:
            print("Lỗi: Vui lòng nhập số!")

while True:
    can_nang = nhap_so("Nhập cân nặng (kg): ")
    chieu_cao = nhap_so("Nhập chiều cao (m): ")
    
    try:
        bmi = tinh_bmi(can_nang, chieu_cao)
        break
    except ZeroDivisionError:
        print("Lỗi: Chiều cao không được bằng 0! Vui lòng nhập lại.\n")


loai = phan_loai(bmi)

print(f"\nBMI của bạn là: {bmi:.2f}")
print("Phân loại:", loai)