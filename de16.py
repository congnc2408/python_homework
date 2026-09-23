
def bai1_nhap_danh_sach():
    danh_sach = {}
    print("--- 1. Nhập danh sách sinh viên ---")
    while True:
        try:
            n = int(input("Nhập số lượng sinh viên n (0 < n < 50): "))
            if 0 < n < 50:
                break
            else:
                print("   -> Lỗi: n phải thỏa mãn điều kiện 0 < n < 50. Vui lòng nhập lại.")
        except ValueError:
            print("   -> Lỗi: Vui lòng nhập một số nguyên hợp lệ.")
            
    for i in range(1, n + 1):
        print(f"\nNhập thông tin sinh viên thứ {i}:")
        ten = input("  - Tên sinh viên: ").strip()
        while True:
            try:
                diem = float(input(f"  - Điểm của {ten}: "))
                if 0 <= diem <= 10:
                    danh_sach[ten] = diem
                    break
                else:
                    print("     -> Lỗi: Điểm phải nằm trong khoảng từ 0 đến 10.")
            except ValueError:
                print("     -> Lỗi: Vui lòng nhập giá trị số thực hoặc số nguyên cho điểm.")
                
    return danh_sach


def bai2_diem_trung_binh(danh_sach):
    if not danh_sach:
        print("2. Danh sách lớp trống.")
        return 0
    dtb = sum(danh_sach.values()) / len(danh_sach)
    print(f"2. Điểm trung bình của tất cả sinh viên trong lớp: {dtb:.2f}")
    return dtb

def bai3_sv_diem_cao_nhat(danh_sach):
    if not danh_sach:
        print("3. Danh sách lớp trống.")
        return []
    diem_max = max(danh_sach.values())
    sv_max = [ten for ten, diem in danh_sach.items() if diem == diem_max]
    print(f"3. Sinh viên có điểm cao nhất ({diem_max}): {', '.join(sv_max)}")
    return sv_max

def bai4_xoa_sv_co_van_oa(danh_sach):

    danh_sach_moi = danh_sach.copy()
    sv_can_xoa = [ten for ten in danh_sach_moi.keys() if "oa" in ten.lower()]
    
    for ten in sv_can_xoa:
        del danh_sach_moi[ten]
        
    if sv_can_xoa:
        print(f"4. Đã xóa các sinh viên có vần 'oa' trong tên ({', '.join(sv_can_xoa)}).")
    else:
        print("4. Không tìm thấy sinh viên nào có vần 'oa' trong tên để xóa.")
        
    print(f"   Danh sách sau khi xóa: {danh_sach_moi}")
    return danh_sach_moi

def main():
    print("--- CHƯƠNG TRÌNH QUẢN LÝ ĐIỂM SINH VIÊN (ĐỀ 16) ---\n")
    
    lop_hoc = bai1_nhap_danh_sach()
    print(f"\n=> Danh sách sinh viên ban đầu: {lop_hoc}\n")
    
    if not lop_hoc:
        print("Chương trình kết thúc vì danh sách trống.")
        return
    bai2_diem_trung_binh(lop_hoc)
    print()
    
    bai3_sv_diem_cao_nhat(lop_hoc)
    print()
    
    bai4_xoa_sv_co_van_oa(lop_hoc)

if __name__ == "__main__":
    main()