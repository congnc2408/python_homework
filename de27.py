
def bai1_nhap_ho_ten():
    ho_ten = input("1. Nhập vào họ tên một người: ")
    print(f"   => Họ tên vừa nhập: '{ho_ten}'")
    return ho_ten

def bai2_chuan_hoa_ho_ten(ho_ten):
    chuan_hoa = " ".join(ho_ten.strip().split()).title()
    print(f"2. Họ tên sau khi chuẩn hóa: '{chuan_hoa}'")
    return chuan_hoa

def bai3_kiem_tra_van_en(ho_ten):
    co_en = "en" in ho_ten.lower()
    if co_en:
        print(f"3. Họ tên '{ho_ten}' CÓ chứa vần 'en'.")
    else:
        print(f"3. Họ tên '{ho_ten}' KHÔNG chứa vần 'en'.")
    return co_en

def bai4_kiem_tra_ten_thanh(ho_ten):
    ds_tu = " ".join(ho_ten.strip().split()).split()
    if not ds_tu:
        print("4. Họ tên trống.")
        return False
    
    ten_chinh = ds_tu[-1] # Lấy từ cuối cùng làm tên
    la_thanh = ten_chinh.lower() == "thanh"
    if la_thanh:
        print("4. Người này CÓ tên là 'Thanh'.")
    else:
        print(f"4. Người này KHÔNG phải tên 'Thanh'. Tên đúng của người này là: '{ten_chinh}'")
    return la_thanh

def bai5_chuan_hoa_ho_ten_lai(ho_ten):
    chuan_hoa = " ".join(ho_ten.strip().split()).title()
    print(f"5. Chuẩn hóa họ tên (lần 2): '{chuan_hoa}'")
    return chuan_hoa

def bai6_cho_biet_ten(ho_ten):
    ds_tu = " ".join(ho_ten.strip().split()).split()
    if not ds_tu:
        print("6. Họ tên trống.")
        return ""
    ten = ds_tu[-1]
    print(f"6. Tên của người vừa nhập là: '{ten}'")
    return ten

def bai7_dem_phu_am_nguyen_am(ho_ten):
    ds_tu = " ".join(ho_ten.strip().split()).split()
    if not ds_tu:
        print("7. Họ tên trống.")
        return 0, 0
    
    ten = ds_tu[-1]
    nguyen_am_set = "ueoaiüöäaeiouáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵ"
    
    chu_cai = [c for c in ten.lower() if c.isalpha()]
    so_nguyen_am = sum(1 for c in chu_cai if c in nguyen_am_set)
    so_phu_am = len(chu_cai) - so_nguyen_am
    
    print(f"7. Trong tên '{ten}':")
    print(f"   - Số nguyên âm: {so_nguyen_am}")
    print(f"   - Số phụ âm: {so_phu_am}")
    return so_nguyen_am, so_phu_am

def main():
    print("--- CHƯƠNG TRÌNH XỬ LÝ HỌ TÊN (ĐỀ 27) ---\n")

    ho_ten = bai1_nhap_ho_ten()
    print()
    
    if not ho_ten.strip():
        print("Họ tên trống. Kết thúc chương trình.")
        return

    bai2_chuan_hoa_ho_ten(ho_ten)
    print()

    bai3_kiem_tra_van_en(ho_ten)
    print()

    bai4_kiem_tra_ten_thanh(ho_ten)
    print()
    
    bai5_chuan_hoa_ho_ten_lai(ho_ten)
    print()

    bai6_cho_biet_ten(ho_ten)
    print()
    
    bai7_dem_phu_am_nguyen_am(ho_ten)

if __name__ == "__main__":
    main()