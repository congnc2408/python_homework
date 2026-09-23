import math

def bai1_nhap_day_so():
    lst = []
    print("1. Nhập dãy số nguyên (nhập 'q' hoặc chữ cái bất kỳ để dừng):")
    while True:
        val = input("   Nhập số: ")

        if val.lower() == 'q' or not val.lstrip('-').isdigit():
            break
        lst.append(int(val))
    print(f"=> Dãy vừa nhập ra màn hình: {lst}")
    return lst

def bai2_min_chan(lst):
    so_chan = [x for x in lst if x % 2 == 0]
    if so_chan:
        min_val = min(so_chan)
        print(f"2. Phần tử nhỏ nhất trong các số chẵn là: {min_val}")
        return min_val
    else:
        print("2. Không có số chẵn nào trong danh sách.")
        return None


def bai3_xoa_so_dau(lst):
    
    lst_copy = lst.copy()
    if lst_copy:
        gia_tri_xoa = lst_copy.pop(0)
        print(f"3. Đã xóa số đầu tiên ({gia_tri_xoa}). Danh sách mới: {lst_copy}")
    else:
        print("3. Danh sách trống, không thể xóa.")
    return lst_copy

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def bai4_dem_nguyen_to(lst):
    so_nguyen_to = [x for x in lst if la_so_nguyen_to(x)]
    dem = len(so_nguyen_to)
    print(f"4. Số lượng số nguyên tố trong danh sách: {dem} (bao gồm: {so_nguyen_to})")
    return dem

def main():
    print("--- CHƯƠNG TRÌNH XỬ LÝ DANH SÁCH (ĐỀ 15) ---\n")
    

    danh_sach = bai1_nhap_day_so()
    print()
    
    if not danh_sach:
        print("Chương trình dừng vì danh sách trống.")
        return

    bai2_min_chan(danh_sach)
    print()
    

    danh_sach_sau_xoa = bai3_xoa_so_dau(danh_sach)
    print()
    
    bai4_dem_nguyen_to(danh_sach)

if __name__ == "__main__":
    main()