import random
import time

def chon_tu():
    danh_sach = ["python", "apple", "river"]
    return random.choice(danh_sach)

def hien_thi_tu(tu, da_doan):
    ket_qua = ""
    
    for ch in tu:
        if ch in da_doan:
            ket_qua += ch + " "
        else:
            ket_qua += "_ "
    
    return ket_qua.strip()


def ghi_file(so_luot_con_lai, thoi_gian):
    file = open("ket_qua.txt", "w", encoding="utf-8")
    
    file.write(f"Số lượt sai còn lại: {so_luot_con_lai}\n")
    file.write(f"Thời gian chơi: {thoi_gian:.2f} giây\n")
    
    file.close()


def game():
    tu = chon_tu()
    da_doan = []
    max_sai = 5
    
    start_time = time.time()
    
    print("===== MINI HANGMAN =====")
    
    while max_sai > 0:
        hien = hien_thi_tu(tu, da_doan)
        print("\nTừ cần đoán:", hien)
        print("Số lượt sai còn lại:", max_sai)
        
        if "_" not in hien:
            print("Chúc mừng! Bạn đã đoán đúng từ:", tu)
            break
        
        chu = input("Nhập chữ cái: ").lower()

        if len(chu) != 1 or not chu.isalpha():
            print("Vui lòng nhập 1 chữ cái!")
            continue
        
        if chu in da_doan:
            print("Bạn đã đoán chữ này rồi!")
            continue
        
        da_doan.append(chu)
        
        if chu in tu:
            print("Đúng!")
        else:
            print("Sai!")
            max_sai -= 1
    
    end_time = time.time()
    thoi_gian = end_time - start_time
    
    if max_sai == 0:
        print("\nBạn thua! Từ đúng là:", tu)
    
    ghi_file(max_sai, thoi_gian)

game()