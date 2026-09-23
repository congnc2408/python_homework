
def bai1_nhap_tuple():
    chuoi = input("Nhập chuỗi số nguyên, cách nhau bằng dấu phẩy: ")
    return tuple(int(x.strip()) for x in chuoi.split(','))


def bai2_in_tuple(tup):
    print(f"Tuple hiện tại: {tup}")

def bai3_in_nua_tuple(tup):
    mid = len(tup) // 2
    nua_dau = tup[:mid]
    nua_cuoi = tup[mid:]
    print(f"Nửa đầu: {nua_dau}")
    print(f"Nửa cuối: {nua_cuoi}")


def bai4_in_chan_le(tup):
    chan = tuple(x for x in tup if x % 2 == 0)
    le = tuple(x for x in tup if x % 2 != 0)
    print(f"Các số chẵn: {chan}")
    print(f"Các số lẻ: {le}")


def bai5_xoa_x(tup, x):
    
    tup_moi = tuple(val for val in tup if val != x)
    if len(tup_moi) < len(tup):
        print(f"Đã xóa phần tử {x} khỏi tuple.")
    else:
        print(f"Phần tử {x} không tồn tại trong tuple.")
    return tup_moi

def bai6_in_max(tup):
    if not tup:
        print("Tuple rỗng, không có số lớn nhất.")
        return None
    gia_tri_max = max(tup)
    print(f"Số lớn nhất trong tuple: {gia_tri_max}")
    return gia_tri_max

def bai7_thay_am_bang_0(tup):
    tup_moi = tuple(0 if x < 0 else x for x in tup)
    return tup_moi


def bai8_tach_hai_tuple(tup):
    tup_chan = tuple(x for x in tup if x % 2 == 0)
    tup_le = tuple(x for x in tup if x % 2 != 0)
    return tup_chan, tup_le


def main():
    print("--- CHƯƠNG TRÌNH XỬ LÝ TUPLE (ĐỀ 5) ---\n")
    

    my_tuple = bai1_nhap_tuple()
    

    print("\n2.", end=" ")
    bai2_in_tuple(my_tuple)
    
    if not my_tuple:
        print("Tuple rỗng, kết thúc chương trình.")
        return


    print("\n3. Chia đôi tuple:")
    bai3_in_nua_tuple(my_tuple)
    

    print("\n4. Trích xuất chẵn/lẻ:")
    bai4_in_chan_le(my_tuple)
    

    try:
        x = int(input("\n5. Nhập số nguyên X cần xóa khỏi tuple: "))
        my_tuple = bai5_xoa_x(my_tuple, x)
        bai2_in_tuple(my_tuple)
    except ValueError:
        pass
    

    print("\n6.", end=" ")
    bai6_in_max(my_tuple)
    

    print("\n7. Thay số âm bằng 0:")
    my_tuple = bai7_thay_am_bang_0(my_tuple)
    bai2_in_tuple(my_tuple)

    print("\n8. Tách tuple ban đầu thành 2 tuple riêng biệt:")
    tup_chan, tup_le = bai8_tach_hai_tuple(my_tuple)
    print(f"   - Tuple chẵn: {tup_chan}")
    print(f"   - Tuple lẻ: {tup_le}")

if __name__ == "__main__":
    main()
