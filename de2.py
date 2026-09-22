from ast import main
def bai1_nhap_day_so():
    lst = []
    print("--- Nhập dãy số nguyên (nhập 'q' hoặc chữ cái bất kỳ để dừng) ---")
    while True:
        val = input("Nhập số: ")
        if val.lower() == 'q' or not val.lstrip('-').isdigit():
            break
        lst.append(int(val))
    print(f"Dãy vừa nhập ra màn hình: {lst}")
    return lst

def bai2_xoa_am(lst):
    return [x for x in lst if x >= 0]

def bai3_dem_x (lst, x):
    return lst.count(x)

def bai4_vi_tri_x(lst,x):
    return [i for i,val in enumerate(lst) if val == x]

def bai5_dem_phan_tu_khac_nhau(lst):
    return len(set(lst))
    
def bai6_xoa_toan_bo():
    return []

def bai7_tbc_chia_het_cho_3(lst):
    chia_3 = [x for x in lst if x % 3 ==0]
    if not chia_3:
        return 0
    return sum(chia_3)/ len(chia_3)

def bai8_xoa_duong(lst):
    return [x for  x in lst if x <= 0]

def bai9_chia_het_cho_5_cuoi_cung(lst):
    for x in reversed(lst):
        if x % 5 == 0:
            return x
    return None

def bai10_tbc_am(lst):
    am = [x for x in lst if x <0]
    if not am:
        return 0
    return sum(am)/ len(am)

def bai11_thay_am_bang_0(lst):
   return  [0 if x < 0 else x for x in lst]

def bai12_xoa_trung_lap(lst):
    ketqua = []
    for x in lst:
        if x not in ketqua:
            ketqua.append(x)
    return ketqua

def bai13_duong_nho_nhat(lst):
    duong = [x for x in lst if x > 0] 
    if not duong:
        return None
    return min(duong) 

def bai14_so_am_lien_tiep_max(lst):
    max_len = 0
    curr_len = 0 
    for x in lst:
        if x < 0 :
            curr_len +=1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 0 
    return max_len

def bai15_tong_va_tbc(lst):
    if not lst:
        return 0, 0
    tong = sum(lst)
    tbc = tong / len(lst)
    return tong, tbc

def la_so_hoan_hao(n):
    if n < 2:
        return False
    tong_uoc = 1
    for i in range(2, int(n**0.5)+1):
        if n % i == 0 :
            tong_uoc += i
            if i != n  //i:
                tong_uoc += n // i
    return tong_uoc == n

def bai16_in_so_hoan_hao(lst):
    hoan_hao = [x for x in lst if la_so_hoan_hao(x)]
    print(f"Các số hoàn hảo trong danh sách: {hoan_hao}")

def main():
    print("--- CHƯƠNG TRÌNH GIẢI ĐỀ 2 ---")
    danh_sach = bai1_nhap_day_so()
    if not danh_sach:
        print("Danh sách trống. Vui lòng chạy lại chương trình và nhập dữ liệu.")
        return
    print(f"\n2. Danh sách sau khi xóa phần tử âm: {bai2_xoa_am(danh_sach)}")

    try:
        x_bai34 = int(input("\nNhập số X để kiểm tra (Câu 3 & 4): "))
        print(f"3. Số lần {x_bai34} xuất hiện: {bai3_dem_x(danh_sach, x_bai34)}")
        print(f"4. Các vị trí xuất hiện của {x_bai34}: {bai4_vi_tri_x(danh_sach, x_bai34)}")
    except ValueError:
        pass

    print(f"\n5. Số phần tử khác nhau: {bai5_dem_phan_tu_khac_nhau(danh_sach)}")

    print(f"7. Trung bình cộng các số chia hết cho 3: {bai7_tbc_chia_het_cho_3(danh_sach)}")

    print(f"8. Danh sách sau khi xóa số dương: {bai8_xoa_duong(danh_sach)}")

    so_chia_5 = bai9_chia_het_cho_5_cuoi_cung(danh_sach)
    print(f"9. Số chia hết cho 5 cuối cùng: {so_chia_5 if so_chia_5 is not None else 'Không có'}")
    print(f"10. Trung bình cộng các số âm: {bai10_tbc_am(danh_sach)}")
    print(f"11. Danh sách khi thay số âm bằng 0: {bai11_thay_am_bang_0(danh_sach)}")
    print(f"12. Danh sách sau khi xóa trùng lặp: {bai12_xoa_trung_lap(danh_sach)}")
    duong_min = bai13_duong_nho_nhat(danh_sach)
    print(f"13. Phần tử dương nhỏ nhất: {duong_min if duong_min is not None else 'Không có'}")
    print(f"14. Số lượng số âm liên tiếp nhiều nhất: {bai14_so_am_lien_tiep_max(danh_sach)}")
    tong, tbc = bai15_tong_va_tbc(danh_sach)
    print(f"15. Tổng danh sách: {tong}, Trung bình cộng: {tbc}")
    print("16.", end=" ")
    bai16_in_so_hoan_hao(danh_sach)
    print(f"\n6. Danh sách sau khi dùng hàm xóa toàn bộ: {bai6_xoa_toan_bo()}")
if __name__ == "__main__":
    main()