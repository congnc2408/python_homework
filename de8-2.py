
def bai1_nhap_thong_tin():
    danh_sach = {}
    print("--- Nhập thông tin học sinh (Nhập 'q' ở tên để dừng) ---")
    while True:
        ten = input("Nhập tên học sinh: ")
        if ten.lower() == 'q':
            break
        
        while True:
            try:
                diem = float(input(f"Nhập điểm cho {ten} (0 đến 10): "))
                if 0 <= diem <= 10:
                    danh_sach[ten] = diem
                    break
                else:
                    print("   -> Lỗi: Điểm phải từ 0 đến 10. Vui lòng nhập lại.")
            except ValueError:
                print("   -> Lỗi: Vui lòng nhập một số hợp lệ.")
    return danh_sach


def bai2_thong_ke_duoi_5(danh_sach):
    dem = sum(1 for diem in danh_sach.values() if diem < 5)
    print(f"2. Số học sinh có điểm nhỏ hơn 5: {dem}")
    return dem


def bai3_danh_sach_gioi(danh_sach):
    ds_gioi = [ten for ten, diem in danh_sach.items() if diem >= 8]
    print(f"3. Danh sách học sinh đạt điểm giỏi (>=8): {ds_gioi}")
    return ds_gioi

def bai4_diem_trung_binh(danh_sach):
    if not danh_sach:
        return 0
    dtb = sum(danh_sach.values()) / len(danh_sach)
    print(f"4. Điểm trung bình của cả lớp: {dtb:.2f}")
    return dtb

def bai5_sv_diem_cao_nhat(danh_sach):
    if not danh_sach:
        print("5. Danh sách trống.")
        return []
    diem_max = max(danh_sach.values())
    sv_max = [ten for ten, diem in danh_sach.items() if diem == diem_max]
    print(f"5. Sinh viên có điểm cao nhất ({diem_max}): {', '.join(sv_max)}")
    return sv_max

def bai6_thong_ke_loai(danh_sach):
    gioi = kha = trung_binh = yeu = 0
    for diem in danh_sach.values():
        if diem >= 8.0:
            gioi += 1
        elif 6.0 <= diem < 8.0:
            kha += 1
        elif 5.0 <= diem < 6.0:
            trung_binh += 1
        else:
            yeu += 1
    
    print("6. Thống kê xếp loại:")
    print(f"   - Giỏi (điểm >= 8.0): {gioi}")
    print(f"   - Khá (8.0 > điểm >= 6.0): {kha}")
    print(f"   - Trung bình (6.0 > điểm >= 5.0): {trung_binh}")
    print(f"   - Yếu (5.0 > điểm): {yeu}")
    return gioi, kha, trung_binh, yeu

def bai7_them_hoc_sinh(danh_sach):
    print("\n7. Thêm 1 học sinh mới:")
    ten = input("   Nhập tên học sinh: ")
    while True:
        try:
            diem = float(input(f"   Nhập điểm cho {ten} (0-10): "))
            if 0 <= diem <= 10:
                danh_sach[ten] = diem
                print(f"   Đã thêm '{ten}' với điểm {diem}.")
                break
            else:
                print("   -> Lỗi: Điểm phải từ 0 đến 10.")
        except ValueError:
            print("   -> Lỗi: Dữ liệu không hợp lệ.")
    return danh_sach

def main():
    print("--- CHƯƠNG TRÌNH QUẢN LÝ LỚP HỌC (ĐỀ 8 - BẢN 2) ---\n")

    lop_hoc = bai1_nhap_thong_tin()
    print(f"\n=> Danh sách hiện tại: {lop_hoc}\n")
    
    if not lop_hoc:
        print("Chưa có dữ liệu học sinh. Kết thúc chương trình.")
        return
    bai2_thong_ke_duoi_5(lop_hoc)

    bai3_danh_sach_gioi(lop_hoc)

    bai4_diem_trung_binh(lop_hoc)

    bai5_sv_diem_cao_nhat(lop_hoc)

    bai6_thong_ke_loai(lop_hoc)

    lop_hoc = bai7_them_hoc_sinh(lop_hoc)
    print(f"\n=> Danh sách sau khi cập nhật: {lop_hoc}")

if __name__ == "__main__":
    main()