def tach_tu(van_ban):
    van_ban = van_ban.lower()

    van_ban = van_ban.replace(",", "")
    van_ban = van_ban.replace(".", "")

    words = van_ban.split()
    
    return words


def dem_so_tu(words):
    return len(words)


def tim_tu_xuat_hien_nhieu_nhat(words):
    tan_suat = {}

    for word in words:
        if word in tan_suat:
            tan_suat[word] += 1
        else:
            tan_suat[word] = 1

    tu_max = None
    max_count = 0
    
    for word in tan_suat:
        if tan_suat[word] > max_count:
            max_count = tan_suat[word]
            tu_max = word
    
    return tu_max, max_count

van_ban = input("Nhập đoạn văn: ")

words = tach_tu(van_ban)

print("\nDanh sách từ:")
print(words)

tong = dem_so_tu(words)
print("Tổng số từ:", tong)

tu_max, so_lan = tim_tu_xuat_hien_nhieu_nhat(words)

print(f"Từ xuất hiện nhiều nhất: '{tu_max}' ({so_lan} lần)")