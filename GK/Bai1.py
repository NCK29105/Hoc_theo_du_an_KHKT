def nhap_cong_viec():
    danh_sach = []
    
    n = int(input("Nhập số lượng công việc: "))
    
    for i in range(n):
        cv = input(f"Nhập công việc {i+1}: ")
        danh_sach.append(cv)
    
    return danh_sach


def hien_thi(danh_sach):
    print("\n DANH SÁCH CÔNG VIỆC : ")
    
    for i in range(len(danh_sach)):
        print(f"{i+1}. {danh_sach[i]}")


def ghi_file(danh_sach):
    file = open("todo_list.txt", "w", encoding="utf-8")
    
    for i in range(len(danh_sach)):
        file.write(f"{i+1}. {danh_sach[i]}\n")
    
    file.close()

ds = nhap_cong_viec()

hien_thi(ds)

ghi_file(ds)

print("\nĐã lưu vào file todo_list.txt!")