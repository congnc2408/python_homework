import math
from collections import Counter

def bai1_nhap_danh_sach():
    chuoi = input("1. Nhập dãy số nguyên, cách nhau bằng dấu phẩy: ")
    try:
        return [int(x.strip()) for x in chuoi.split(',')]
    except ValueError:
        print("   -> Lỗi: Dữ liệu nhập vào không hợp lệ.")
        return []

def bai2_max_chia_het_cho_3(lst):
    chia_het_3 = [x for x in lst if x % 3 == 0]
    if chia_het_3:
        max_val = max(chia_het_3)
        print(f"2. Số lớn nhất chia hết cho 3 là: {max_val}")
        return max_val
    else:
        print("2. Không có số nào chia hết cho 3 trong danh sách.")
        return None

def la_so_chinh_phuong(n):
    if n < 0:
        return False
    return int(math.isqrt(n))**2 == n

def bai3_in_so_chinh_phuong(lst):
    chinh_phuong = [x for x in lst if la_so_chinh_phuong(x)]
    print(f"3. Các số chính phương có trong danh sách: {chinh_phuong}")
    return chinh_phuong

def bai4_tim_vi_tri_cuoi_cua_x(lst):
    try:
        x = int(input("\n4. Nhập số nguyên X cần tìm: "))
        if x in lst:
            
            vi_tri_cuoi = max(i for i, val in enumerate(lst) if val == x)
            print(f"   => Số {x} có trong danh sách. Vị trí cuối cùng (index) là: {vi_tri_cuoi}")
            return vi_tri_cuoi
        else:
            print(f"   => Số {x} KHÔNG có trong danh sách.")
            return -1
    except ValueError:
        print("   -> Lỗi: Vui lòng nhập một số nguyên.")
        return -1

def bai5_min_duong(lst):
    so_duong = [x for x in lst if x > 0]
    if so_duong:
        min_val = min(so_duong)
        print(f"5. Số nhỏ nhất trong các số dương là: {min_val}")
        return min_val
    else:
        print("5. Không có số dương nào trong danh sách.")
        return None

def bai6_giai_thua(lst):
    giai_thua_list = []
    for x in lst:
        if x >= 0:
            giai_thua_list.append(math.factorial(x))
        else:
            giai_thua_list.append("Không xác định (số âm)")
    print(f"6. Giai thừa của các số trong danh sách:\n   {giai_thua_list}")
    return giai_thua_list

def bai7_xoa_x(lst):
    lst_copy = lst.copy()
    try:
        x = int(input("\n7. Nhập số nguyên X cần xóa: "))
        if x in lst_copy:

            lst_copy = [val for val in lst_copy if val != x]
            print(f"   => Đã xóa số {x}. Danh sách mới: {lst_copy}")
        else:
            print(f"   => Số {x} KHÔNG có trong danh sách để xóa.")
        return lst_copy
    except ValueError:
        print("   -> Lỗi: Vui lòng nhập một số nguyên.")
        return lst_copy


def bai8_tbc_chia_het_cho_3(lst):
    chia_het_3 = [x for x in lst if x % 3 == 0]
    if chia_het_3:
        tbc = sum(chia_het_3) / len(chia_het_3)
        print(f"8. Trung bình cộng các số chia hết cho 3 là: {tbc}")
        return tbc
    else:
        print("8. Không có số nào chia hết cho 3 để tính TBC.")
        return 0

def bai9_so_xuat_hien_nhieu_nhat(lst):
    if not lst:
        print("9. Danh sách trống.")
        return []
    dem = Counter(lst)
    max_count = max(dem.values())
    ket_qua = [k for k, v in dem.items() if v == max_count]
    print(f"9. (Các) số xuất hiện nhiều nhất (số lần: {max_count}): {ket_qua}")
    return ket_qua

def bai10_xoa_vi_tri_thu_3(lst):
    lst_copy = lst.copy()

    if len(lst_copy) >= 3:
        gia_tri_bi_xoa = lst_copy.pop(2)
        print(f"10. Đã xóa phần tử ở vị trí thứ 3 (index 2), giá trị là {gia_tri_bi_xoa}.")
        print(f"    Danh sách mới: {lst_copy}")
    else:
        print("10. Danh sách không đủ 3 phần tử để xóa.")
    return lst_copy



def main():
    print("--- CHƯƠNG TRÌNH XỬ LÝ DANH SÁCH (ĐỀ 12) ---\n")
    

    danh_sach = bai1_nhap_danh_sach()
    print(f"=> Danh sách hiện tại: {danh_sach}\n")
    
    if not danh_sach:
        print("Chương trình dừng vì danh sách trống.")
        return


    bai2_max_chia_het_cho_3(danh_sach)
    

    bai3_in_so_chinh_phuong(danh_sach)

    bai4_tim_vi_tri_cuoi_cua_x(danh_sach)
    print()
    

    bai5_min_duong(danh_sach)

    bai6_giai_thua(danh_sach)
    

    danh_sach_sau_xoa = bai7_xoa_x(danh_sach)
    print()

    bai8_tbc_chia_het_cho_3(danh_sach)
    
    bai9_so_xuat_hien_nhieu_nhat(danh_sach)
    
    danh_sach_cuoi = bai10_xoa_vi_tri_thu_3(danh_sach)

if __name__ == "__main__":
    main()