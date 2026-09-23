
def bai1_nhap_danh_sach_ten():
    chuoi = input("1. Nhập dãy họ tên học sinh, cách nhau bởi dấu phẩy: ")
    return [ten.strip() for ten in chuoi.split(',') if ten.strip()]

def bai2_ten_dai_nhat(danh_sach):
    if not danh_sach:
        print("2. Danh sách trống.")
        return []
    
    max_len = len(max(danh_sach, key=len))
    ten_dai = [ten for ten in danh_sach if len(ten) == max_len]
    print(f"2. (Các) học sinh có tên dài nhất ({max_len} ký tự): {', '.join(ten_dai)}")
    return ten_dai

def bai3_ten_ngan_nhat(danh_sach):
    if not danh_sach:
        print("3. Danh sách trống.")
        return []

    min_len = len(min(danh_sach, key=len))
    ten_ngan = [ten for ten in danh_sach if len(ten) == min_len]
    print(f"3. (Các) học sinh có tên ngắn nhất ({min_len} ký tự): {', '.join(ten_ngan)}")
    return ten_ngan

def bai4_sap_xep_alphabet(danh_sach):

    danh_sach_sap_xep = sorted(danh_sach)
    print(f"4. Danh sách sắp xếp theo Alphabet: {danh_sach_sap_xep}")
    return danh_sach_sap_xep

def bai5_xu_ly_ten_trung(danh_sach):

    if len(set(danh_sach)) < len(danh_sach):
        print("5. Phát hiện có họ tên bị lặp trong danh sách!")

        danh_sach_moi = list(dict.fromkeys(danh_sach))
        print(f"   => Danh sách sau khi loại bỏ tên trùng: {danh_sach_moi}")
        return danh_sach_moi
    else:
        print("5. Không có họ tên nào bị lặp trong danh sách.")
        return danh_sach


def main():
    print("--- CHƯƠNG TRÌNH XỬ LÝ DANH SÁCH HỌ TÊN (ĐỀ 13) ---\n")
    
    danh_sach_lop = bai1_nhap_danh_sach_ten()
    print(f"\n=> List họ tên hiện tại: {danh_sach_lop}\n")
    
    if not danh_sach_lop:
        print("Chương trình kết thúc vì danh sách trống.")
        return

    bai2_ten_dai_nhat(danh_sach_lop)
    

    bai3_ten_ngan_nhat(danh_sach_lop)
    

    bai4_sap_xep_alphabet(danh_sach_lop)

    danh_sach_lop_cuoi = bai5_xu_ly_ten_trung(danh_sach_lop)

if __name__ == "__main__":
    main()