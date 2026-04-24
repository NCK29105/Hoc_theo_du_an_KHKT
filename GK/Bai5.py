import matplotlib.pyplot as plt

def nhap_so_luong():
    while True:
        try:
            so_luong = int(input("Nhập số lượng Ví da: "))
            return so_luong
        except:
            print("Lỗi: Vui lòng nhập số!")


def cap_nhat_kho(kho):
    so_luong_vi = nhap_so_luong()
    kho["Vi da"] = so_luong_vi

    if "Balo" in kho:
        kho["Balo"] -= 30
    
    return kho


def ve_bieu_do(kho):
    ten = list(kho.keys())
    so_luong = list(kho.values())
    
    plt.pie(so_luong, labels=ten, autopct='%1.1f%%')
    plt.title("Tỷ trọng hàng trong kho")
    
    plt.show()

kho = {
    'Balo': 150,
    'Tui xach': 80,
    'Vali': 120
}

print("Kho ban đầu:", kho)

kho = cap_nhat_kho(kho)

print("\nKho sau khi cập nhật:", kho)

ve_bieu_do(kho)