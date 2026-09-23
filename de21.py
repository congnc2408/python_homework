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

def bai2_dem_nguoi_dung(tai_khoan):
    tong_so = len(tai_khoan)
    print(f"2. Tổng số người dùng trong hệ thống: {tong_so}")
    return tong_so

def bai3_tim_ten_theo_mat_khau(tai_khoan):
    print("\n3. Tìm tên người dùng theo mật khẩu:")
    mk_can_tim = input("   Nhập mật khẩu cần tìm: ").strip()
    nguoi_tim_thay = [ten for ten, mk in tai_khoan.items() if mk == mk_can_tim]
    
    if nguoi_tim_thay:
        print(f"   => Tên người dùng có mật khẩu '{mk_can_tim}' là: {', '.join(nguoi_tim_thay)}")
    else:
        print(f"   => Không tìm thấy người dùng nào có mật khẩu '{mk_can_tim}'.")
    return nguoi_tim_thay

def bai4_mat_khau_3_chu_cai(tai_khoan):
    print("\n4. Các người dùng có mật khẩu có đúng 3 chữ cái:")
    ds_phu_hop = [ten for ten, mk in tai_khoan.items() if len(mk) == 3 and mk.isalpha()]
    
    if ds_phu_hop:
        for ten in ds_phu_hop:
            print(f"   - Tên: {ten}, Mật khẩu: '{tai_khoan[ten]}'")
    else:
        print("   => Không có người dùng nào có mật khẩu chứa đúng 3 chữ cái.")
    return ds_phu_hop

def main():
    print("--- CHƯƠNG TRÌNH QUẢN LÝ TÀI KHOẢN (ĐỀ 21) ---\n")
    
    danh_sach_tk = bai1_nhap_thong_tin()
    print(f"\n=> Danh sách tài khoản vừa nhập: {danh_sach_tk}\n")
    
    if not danh_sach_tk:
        print("Danh sách trống. Kết thúc chương trình.")
        return

    bai2_dem_nguoi_dung(danh_sach_tk)
    
    bai3_tim_ten_theo_mat_khau(danh_sach_tk)

    bai4_mat_khau_3_chu_cai(danh_sach_tk)

if __name__ == "__main__":
    main()