import math
from collections import Counter


def bai1_nhap_danh_sach():
    chuoi = input("Nhập dãy số nguyên, cách nhau bằng dấu phẩy: ")
    return [int(x.strip()) for x in chuoi.split(',')]


def bai2_tong_va_trung_binh(lst):
    if not lst:
        return 0, 0
    tong = sum(lst)
    return tong, tong / len(lst)


def bai3_vi_tri_am_dau_cuoi(lst):
    vi_tri_dau = -1
    vi_tri_cuoi = -1
    for i, val in enumerate(lst):
        if val < 0:
            if vi_tri_dau == -1:
                vi_tri_dau = i
            vi_tri_cuoi = i
    return vi_tri_dau, vi_tri_cuoi


def bai4_so_duong_lien_tiep_max(lst):
    max_len = 0
    curr_len = 0
    for val in lst:
        if val > 0:
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 0
    return max_len


def bai5_danh_sach_chan(lst):
    return [x for x in lst if x % 2 == 0]


def bai6_danh_sach_le(lst):
    return [x for x in lst if x % 2 != 0]


def bai7_max_va_vi_tri_cuoi(lst):
    if not lst:
        return None, -1
    gia_tri_max = max(lst)

    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == gia_tri_max:
            return gia_tri_max, i


def bai8_loai_bo_trung(lst):
    ket_qua = []
    for x in lst:
        if x not in ket_qua:
            ket_qua.append(x)
    return ket_qua


def bai9_sap_xep_tang_dan(lst):
    return sorted(lst)


def bai10_chen_x_giu_tang_dan(lst, x):

    lst_tang = sorted(lst) 
    for i in range(len(lst_tang)):
        if lst_tang[i] >= x:
            lst_tang.insert(i, x)
            return lst_tang
    lst_tang.append(x)
    return lst_tang

def la_so_chinh_phuong(n):
    if n < 0:
        return False
    return int(math.isqrt(n))**2 == n


def bai11_in_so_chinh_phuong(lst):
    chinh_phuong = [x for x in lst if la_so_chinh_phuong(x)]
    print(f"Các số chính phương trong danh sách: {chinh_phuong}")


def bai12_dan_dau_dai_nhat(lst):
    if len(lst) < 2:
        return len(lst)
    max_len = 1
    curr_len = 1
    for i in range(1, len(lst)):

        if lst[i] * lst[i-1] < 0:
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 1
    return max_len


def bai13_dem_so_chinh_phuong(lst):
    return sum(1 for x in lst if la_so_chinh_phuong(x))


def bai14_sap_xep_giam_dan(lst):
    return sorted(lst, reverse=True)

def bai15_xoa_phan_tu_thu_k(lst, k):
    lst_copy = lst.copy()
    if 0 <= k < len(lst_copy):
        lst_copy.pop(k)
        print(f"Đã xóa phần tử tại vị trí (index) {k}.")
    else:
        print("Vị trí k không hợp lệ.")
    return lst_copy


def bai16_dem_so_bi_lap(lst):
    dem = Counter(lst)

    so_luong_bi_lap = sum(1 for k, v in dem.items() if v > 1)
    return so_luong_bi_lap


def bai17_dao_nguoc(lst):
    return lst[::-1]


def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def bai18_in_so_nguyen_to(lst):
    nguyen_to = [x for x in lst if la_so_nguyen_to(x)]
    print(f"Các số nguyên tố trong danh sách: {nguyen_to}")


def bai19_them_x_neu_chua_co(lst, x):
    lst_copy = lst.copy()
    if x not in lst_copy:
        lst_copy.append(x)
        print(f"Đã thêm {x} vào danh sách.")
    else:
        print(f"{x} đã tồn tại trong danh sách.")
    return lst_copy



def main():
    print("--- CHƯƠNG TRÌNH KIỂM THỬ CÁC HÀM ---")
    

    danh_sach = bai1_nhap_danh_sach()
    print(f"Danh sách vừa nhập: {danh_sach}\n")
    

    tong, tb = bai2_tong_va_trung_binh(danh_sach)
    print(f"2. Tổng: {tong}, Trung bình: {tb}")
    

    vt_dau, vt_cuoi = bai3_vi_tri_am_dau_cuoi(danh_sach)
    print(f"3. Vị trí âm đầu tiên: {vt_dau}, Vị trí âm cuối cùng: {vt_cuoi}")
    

    duong_lt_max = bai4_so_duong_lien_tiep_max(danh_sach)
    print(f"4. Số lượng số dương liên tiếp nhiều nhất: {duong_lt_max}")

    print(f"5. Danh sách số chẵn: {bai5_danh_sach_chan(danh_sach)}")
    print(f"6. Danh sách số lẻ: {bai6_danh_sach_le(danh_sach)}")
    

    pt_max, vt_max_cuoi = bai7_max_va_vi_tri_cuoi(danh_sach)
    print(f"7. Phần tử lớn nhất: {pt_max}, Vị trí cuối cùng của nó: {vt_max_cuoi}")
    

    print(f"8. Danh sách sau khi loại bỏ trùng lặp: {bai8_loai_bo_trung(danh_sach)}")
    

    print(f"9. Sắp xếp tăng dần: {bai9_sap_xep_tang_dan(danh_sach)}")

    try:
        x_bai10 = int(input("\nNhập số x để chèn vào danh sách tăng dần (Câu 10): "))
        print(f"10. Danh sách sau khi chèn {x_bai10}: {bai10_chen_x_giu_tang_dan(danh_sach, x_bai10)}")
    except ValueError:
        pass
    

    print("\n11.", end=" ")
    bai11_in_so_chinh_phuong(danh_sach)
    print(f"12. Chuỗi đan dấu dài nhất có độ dài: {bai12_dan_dau_dai_nhat(danh_sach)}")
    print(f"13. Số lượng số chính phương: {bai13_dem_so_chinh_phuong(danh_sach)}")
    

    print(f"14. Sắp xếp giảm dần: {bai14_sap_xep_giam_dan(danh_sach)}")
    

    try:
        k = int(input("\nNhập vị trí k cần xóa (Câu 15): "))
        danh_sach_sau_xoa = bai15_xoa_phan_tu_thu_k(danh_sach, k)
        print(f"    Danh sách mới: {danh_sach_sau_xoa}")
    except ValueError:
        pass

    print(f"16. Số lượng các số bị lặp lại (xuất hiện >1 lần): {bai16_dem_so_bi_lap(danh_sach)}")
    print(f"17. Danh sách đảo ngược: {bai17_dao_nguoc(danh_sach)}")
    print("18.", end=" ")
    bai18_in_so_nguyen_to(danh_sach)

    try:
        x_bai19 = int(input("\nNhập số X để kiểm tra và thêm (Câu 19): "))
        danh_sach = bai19_them_x_neu_chua_co(danh_sach, x_bai19)
        print(f"    Danh sách hiện tại: {danh_sach}")
    except ValueError:
        pass

if __name__ == "__main__":
    main()