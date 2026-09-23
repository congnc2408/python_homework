from collections import Counter

def bai1_nhap_tuple():
    chuoi = input("1. Nhập dãy số nguyên, cách nhau bằng dấu phẩy: ")
    try:
        tup = tuple(int(x.strip()) for x in chuoi.split(','))
        print(f"   => Tuple vừa tạo: {tup}")
        return tup
    except ValueError:
        print("   -> Lỗi: Dữ liệu nhập vào không hợp lệ, vui lòng chỉ nhập các số nguyên.")
        return ()

def bai2_in_nua_tuple(tup):
    if not tup:
        print("2. Tuple rỗng.")
        return
    mid = len(tup) // 2
    nua_dau = tup[:mid]
    nua_cuoi = tup[mid:]
    print(f"2. Nửa đầu tuple: {nua_dau}")
    print(f"   Nửa cuối tuple: {nua_cuoi}")

def bai3_tao_tuple_chan(tup):
    tup_chan = tuple(x for x in tup if x % 2 == 0)
    print(f"3. Tuple chứa các số chẵn: {tup_chan}")
    return tup_chan

def bai4_dem_so_trung_lap(tup):
    if not tup:
        print("4. Tuple rỗng, không có số trùng lặp.")
        return 0
    dem = Counter(tup)
    so_luong_trung = sum(1 for val in dem.values() if val > 1)
    print(f"4. Số lượng giá trị bị lặp lại trong tuple: {so_luong_trung}")
    return so_luong_trung

def main():
    print("--- CHƯƠNG TRÌNH XỬ LÝ TUPLE (ĐỀ 17) ---\n")
    
    my_tuple = bai1_nhap_tuple()
    print()
    
    if not my_tuple:
        print("Chương trình dừng vì tuple trống hoặc nhập sai định dạng.")
        return

    bai2_in_nua_tuple(my_tuple)
    print()
    

    bai3_tao_tuple_chan(my_tuple)
    print()
    
    bai4_dem_so_trung_lap(my_tuple)

if __name__ == "__main__":
    main()