
def bai1_nhap_chi_tieu():
    chi_tieu = {}
    ngay_trong_tuan = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"]
    print("--- 1. Nhập chi tiêu hằng ngày trong tuần ---")
    for ngay in ngay_trong_tuan:
        while True:
            try:
                so_tien = float(input(f"Nhập số tiền chi tiêu ngày {ngay}: "))
                if so_tien >= 0:
                    chi_tieu[ngay] = so_tien
                    break
                else:
                    print("   -> Lỗi: Số tiền chi tiêu không được âm. Vui lòng nhập lại.")
            except ValueError:
                print("   -> Lỗi: Vui lòng nhập một số hợp lệ.")
    return chi_tieu

def bai2_tong_va_trung_binh(chi_tieu):
    if not chi_tieu:
        print("2. Dictionary chi tiêu trống.")
        return 0, 0
    tong = sum(chi_tieu.values())
    tbc = tong / len(chi_tieu)
    print(f"2. Tổng chi tiêu trong tuần: {tong:,.2f}")
    print(f"   Chi tiêu trung bình mỗi ngày: {tbc:,.2f}")
    return tong, tbc

def bai3_max_min_chi_tieu(chi_tieu):
    if not chi_tieu:
        print("3. Dictionary chi tiêu trống.")
        return [], []
    
    max_tien = max(chi_tieu.values())
    min_tien = min(chi_tieu.values())
    
    ngay_max = [ngay for ngay, tien in chi_tieu.items() if tien == max_tien]
    ngay_min = [ngay for ngay, tien in chi_tieu.items() if tien == min_tien]
    
    print(f"3. Ngày chi tiêu nhiều nhất: {', '.join(ngay_max)} ({max_tien:,.2f})")
    print(f"   Ngày chi tiêu ít nhất: {', '.join(ngay_min)} ({min_tien:,.2f})")
    return ngay_max, ngay_min


def bai4_xoa_ngay_cuoi(chi_tieu):
    
    chi_tieu_moi = chi_tieu.copy()
    if chi_tieu_moi:
        ngay_cuoi = list(chi_tieu_moi.keys())[-1]
        del chi_tieu_moi[ngay_cuoi]
        print(f"4. Đã loại bỏ thông tin chi tiêu của ngày cuối cùng ({ngay_cuoi}).")
    else:
        print("4. Dictionary trống.")
        
    print(f"   Dictionary sau khi xóa: {chi_tieu_moi}")
    return chi_tieu_moi

def main():
    print("--- CHƯƠNG TRÌNH QUẢN LÝ CHI TIÊU TUẦN (ĐỀ 18) ---\n")
    
    bang_chi_tieu = bai1_nhap_chi_tieu()
    print(f"\n=> Dữ liệu chi tiêu tuần: {bang_chi_tieu}\n")

    bai2_tong_va_trung_binh(bang_chi_tieu)
    print()

    bai3_max_min_chi_tieu(bang_chi_tieu)
    print()
    bai4_xoa_ngay_cuoi(bang_chi_tieu)

if __name__ == "__main__":
    main()