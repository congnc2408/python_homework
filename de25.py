
def bai1_nhap_can_bo():
    danh_sach = {}
    print("--- 1. Nhập thông tin cán bộ ---")
    while True:
        try:
            n = int(input("Nhập số lượng cán bộ n (0 < n < 20): "))
            if 0 < n < 20:
                break
            else:
                print("   -> Lỗi: n phải thỏa mãn điều kiện 0 < n < 20. Vui lòng nhập lại.")
        except ValueError:
            print("   -> Lỗi: Vui lòng nhập một số nguyên hợp lệ.")
            
    for i in range(1, n + 1):
        print(f"\nNhập thông tin cán bộ thứ {i}:")
        ten = input("  - Tên cán bộ: ").strip()
        while True:
            try:
                tuoi = int(input(f"  - Tuổi của {ten}: "))
                if tuoi > 0:
                    danh_sach[ten] = tuoi
                    break
                else:
                    print("     -> Lỗi: Tuổi phải lớn hơn 0.")
            except ValueError:
                print("     -> Lỗi: Vui lòng nhập số nguyên cho tuổi.")
                
    return danh_sach

def bai2_can_bo_nhieu_tuoi_nhat(danh_sach):
    if not danh_sach:
        print("2. Danh sách cán bộ trống.")
        return []
    tuoi_max = max(danh_sach.values())
    cb_max = [ten for ten, tuoi in danh_sach.items() if tuoi == tuoi_max]
    print(f"2. Cán bộ nhiều tuổi nhất ({tuoi_max} tuổi): {', '.join(cb_max)}")
    return cb_max
def bai3_tuoi_trung_binh(danh_sach):
    if not danh_sach:
        print("3. Danh sách cán bộ trống.")
        return 0
    dtb = sum(danh_sach.values()) / len(danh_sach)
    print(f"3. Độ tuổi trung bình của các cán bộ: {dtb:.2f}")
    return dtb

def bai4_xoa_can_bo_tren_40(danh_sach):
    danh_sach_moi = {ten: tuoi for ten, tuoi in danh_sach.items() if tuoi <= 40}
    print("4. Đã xóa các cán bộ có tuổi lớn hơn 40.")
    print(f"   Danh sách cán bộ sau khi cập nhật: {danh_sach_moi}")
    return danh_sach_moi

def main():
    print("--- CHƯƠNG TRÌNH QUẢN LÝ CÁN BỘ (ĐỀ 25) ---\n")
    
    ds_can_bo = bai1_nhap_can_bo()
    print(f"\n=> Danh sách cán bộ ban đầu: {ds_can_bo}\n")
    
    if not ds_can_bo:
        print("Danh sách trống. Kết thúc chương trình.")
        return

    bai2_can_bo_nhieu_tuoi_nhat(ds_can_bo)
    print()

    bai3_tuoi_trung_binh(ds_can_bo)
    print()
    
    bai4_xoa_can_bo_tren_40(ds_can_bo)

if __name__ == "__main__":
    main()