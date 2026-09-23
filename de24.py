def bai1_nhap_thu_vien():
    thu_vien = {}
    print("--- 1. Nhập thông tin sách (Nhập 'q' ở tên sách để dừng) ---")
    while True:
        ten_sach = input("Nhập tên sách: ").strip()
        if ten_sach.lower() == 'q':
            break
        while True:
            try:
                so_luong = int(input(f"Nhập số lượng cho cuốn '{ten_sach}': "))
                if so_luong >= 0:
                    thu_vien[ten_sach] = so_luong
                    break
                else:
                    print("   -> Lỗi: Số lượng sách không được âm. Vui lòng nhập lại.")
            except ValueError:
                print("   -> Lỗi: Vui lòng nhập một số nguyên hợp lệ.")
    return thu_vien

def bai2_tong_so_sach(thu_vien):
    tong = sum(thu_vien.values())
    print(f"2. Tổng số lượng tất cả các cuốn sách trong thư viện: {tong}")
    return tong

def bai3_sach_10_quyen(thu_vien):
    print("3. Các cuốn sách có số lượng đúng 10 quyển:")
    sach_10 = [ten for ten, sl in thu_vien.items() if sl == 10]
    if sach_10:
        for ten in sach_10:
            print(f"   - {ten}")
    else:
        print("   => Không có cuốn sách nào có số lượng 10 quyển.")
    return sach_10

def bai4_xoa_sach_duoi_5(thu_vien):
    thu_vien_moi = {ten: sl for ten, sl in thu_vien.items() if sl >= 5}
    print("4. Đã xóa các cuốn sách có số lượng dưới 5 quyển.")
    print(f"   Thư viện sau khi cập nhật: {thu_vien_moi}")
    return thu_vien_moi

def main():
    print("--- CHƯƠNG TRÌNH QUẢN LÝ THƯ VIỆN (ĐỀ 24) ---\n")

    thu_vien_sach = bai1_nhap_thu_vien()
    print(f"\n=> Dữ liệu thư viện ban đầu: {thu_vien_sach}\n")
    
    if not thu_vien_sach:
        print("Thư viện trống. Kết thúc chương trình.")
        return

    bai2_tong_so_sach(thu_vien_sach)
    print()
    
    bai3_sach_10_quyen(thu_vien_sach)
    print()
    
    bai4_xoa_sach_duoi_5(thu_vien_sach)

if __name__ == "__main__":
    main()