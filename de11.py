from collections import Counter

def bai1_tao_list():
    while True:
        chuoi = input("1. Nhập danh sách các số nguyên, cách nhau bằng dấu phẩy (yêu cầu 5 < n < 20): ")
        try:
            lst = [int(x.strip()) for x in chuoi.split(',')]
            n = len(lst)
            if 5 < n < 20:
                return lst
            else:
                print(f"   -> Lỗi: Số lượng phần tử là {n}, chưa thỏa mãn điều kiện 5 < n < 20. Vui lòng nhập lại.")
        except ValueError:
            print("   -> Lỗi: Dữ liệu nhập vào không hợp lệ, vui lòng chỉ nhập số nguyên.")

def bai2_chan_xuat_hien_nhieu_nhat(lst):
    chan = [x for x in lst if x % 2 == 0]
    if not chan:
        print("2. Không có số chẵn nào trong danh sách.")
        return []
    
    dem = Counter(chan)
    max_count = max(dem.values())
    ket_qua = [k for k, v in dem.items() if v == max_count]
    print(f"2. (Các) số chẵn xuất hiện nhiều nhất (số lần: {max_count}): {ket_qua}")
    return ket_qua

def bai3_6_le_nho_nhat(lst):
    le = [x for x in lst if x % 2 != 0]
    if not le:
        print("3 & 6. Không có số lẻ nào trong danh sách.")
        return []
    
    min_le = min(le)
    ket_qua = [x for x in le if x == min_le]
    print(f"3 & 6. (Các) số lẻ nhỏ nhất trong danh sách là: {ket_qua} (giá trị: {min_le})")
    return ket_qua

def bai4_thay_the_chia_het_cho_5(lst):
    ket_qua = [5 if x % 5 == 0 else x for x in lst]
    print(f"4. Danh sách sau khi thay số chia hết cho 5 thành 5: {ket_qua}")
    return ket_qua


def bai5_so_xuat_hien_nhieu_nhat(lst):
    if not lst:
        return []
    dem = Counter(lst)
    max_count = max(dem.values())
    ket_qua = [k for k, v in dem.items() if v == max_count]
    print(f"5. (Các) số xuất hiện nhiều nhất trong list (số lần: {max_count}): {ket_qua}")
    return ket_qua


def bai7_xoa_chia_het_cho_3(lst):
    ket_qua = [x for x in lst if x % 3 != 0]
    print(f"7. Danh sách sau khi xóa các số chia hết cho 3: {ket_qua}")
    return ket_qua



def main():
    print("--- CHƯƠNG TRÌNH XỬ LÝ DANH SÁCH (ĐỀ 11) ---\n")
    

    danh_sach = bai1_tao_list()
    print(f"\n=> Danh sách hợp lệ vừa nhập: {danh_sach}\n")

    bai2_chan_xuat_hien_nhieu_nhat(danh_sach)
    

    bai3_6_le_nho_nhat(danh_sach)
    

    bai5_so_xuat_hien_nhieu_nhat(danh_sach)
    

    danh_sach_cau_4 = bai4_thay_the_chia_het_cho_5(danh_sach)

    danh_sach_cau_7 = bai7_xoa_chia_het_cho_3(danh_sach)

if __name__ == "__main__":
    main()