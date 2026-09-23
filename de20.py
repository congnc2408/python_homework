
def bai1_nhap_thong_tin():
    tai_khoan = {}
    print("--- 1. Nhập thông tin tài khoản (Nhập 'q' ở tên để dừng) ---")
    while True:
        ten = input("Nhập tên người dùng: ").strip()
        if ten.lower() == 'q':
            break
        mat_khau = input(f"Nhập mật khẩu cho {ten}: ").strip()
        tai_khoan[ten] = mat_khau
    return tai_khoan
def bai2_kiem_tra_mat_khau_khong_hop_le(tai_khoan):
    print("\n2. Kiểm tra mật khẩu không hợp lệ (Hợp lệ: đúng 7 ký tự và bắt đầu bằng chữ hoa):")
    khong_hop_le = []
    for ten, mk in tai_khoan.items():
        is_valid = len(mk) == 7 and mk[0].isupper()
        if not is_valid:
            khong_hop_le.append((ten, mk))
            
    if khong_hop_le:
        print("   => Các tài khoản có mật khẩu không hợp lệ:")
        for ten, mk in khong_hop_le:
            print(f"      - Tên: {ten}, Mật khẩu: '{mk}'")
    else:
        print("   => Tất cả mật khẩu đều hợp lệ.")
    return khong_hop_le

def bai3_tim_mat_khau(tai_khoan):
    print("\n3. Tìm mật khẩu theo tên người dùng:")
    ten_tim = input("   Nhập tên người dùng cần tìm: ").strip()
    if ten_tim in tai_khoan:
        print(f"   => Mật khẩu của '{ten_tim}' là: {tai_khoan[ten_tim]}")
    else:
        print(f"   => Không tìm thấy người dùng tên '{ten_tim}'.")


def bai4_mat_khau_toan_chu_hoa(tai_khoan):
    print("\n4. Các người dùng có mật khẩu toàn chữ hoa:")
    toan_chu_hoa = [ten for ten, mk in tai_khoan.items() if mk and mk.isupper()]
    
    if toan_chu_hoa:
        print(f"   => Những người dùng có mật khẩu toàn chữ hoa: {', '.join(toan_chu_hoa)}")
        for ten in toan_chu_hoa:
            print(f"      - {ten}: {tai_khoan[ten]}")
    else:
        print("   => Không có người dùng nào có mật khẩu toàn chữ hoa.")
    return toan_chu_hoa

def main():
    print("--- CHƯƠNG TRÌNH QUẢN LÝ TÀI KHOẢN (ĐỀ 20) ---\n")
    
    danh_sach_tk = bai1_nhap_thong_tin()
    print(f"\n=> Danh sách tài khoản vừa nhập: {danh_sach_tk}\n")
    
    if not danh_sach_tk:
        print("Danh sách trống. Kết thúc chương trình.")
        return

    bai2_kiem_tra_mat_khau_khong_hop_le(danh_sach_tk)
    
    bai3_tim_mat_khau(danh_sach_tk)
    
    bai4_mat_khau_toan_chu_hoa(danh_sach_tk)

if __name__ == "__main__":
    main()