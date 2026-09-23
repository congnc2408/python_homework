import math



def la_so_hoan_hao(n):
    if n < 2:
        return False
    tong_uoc = 1
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            tong_uoc += i
            if i != n // i:
                tong_uoc += n // i
    return tong_uoc == n

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def bai1_nhap_tuple():
    while True:
        chuoi = input("1. Nhập chuỗi số nguyên (cách nhau bằng dấu phẩy, yêu cầu 5 < n < 30): ")
        try:
            danh_sach = [int(x.strip()) for x in chuoi.split(',')]
            n = len(danh_sach)
            if 5 < n < 30:
                return tuple(danh_sach)
            else:
                print(f"   -> Lỗi: Số lượng phần tử là {n}, chưa thỏa mãn điều kiện 5 < n < 30. Vui lòng nhập lại.")
        except ValueError:
            print("   -> Lỗi: Dữ liệu nhập vào không hợp lệ, vui lòng chỉ nhập số nguyên.")

def bai2_trung_binh_cong(tup):
    if tup:
        tbc = sum(tup) / len(tup)
        print(f"2. Trung bình cộng các số trong tuple: {tbc}")
        return tbc
    return 0

def bai3_chen_x(tup):
    try:
        x = int(input("\n3. Nhập số nguyên X cần chèn vào tuple: "))
        tup_moi = tup + (x,)
        print(f"   Tuple mới sau khi chèn {x}: {tup_moi}")
        return tup_moi
    except ValueError:
        print("   -> Vui lòng nhập một số nguyên hợp lệ.")
        return tup

def bai4_so_hoan_hao(tup):
    hoan_hao = tuple(x for x in tup if la_so_hoan_hao(x))
    print(f"4. Các số hoàn hảo trong tuple: {hoan_hao}")
    return hoan_hao
def bai5_so_nguyen_to(tup):
    nguyen_to = tuple(x for x in tup if la_so_nguyen_to(x))
    print(f"5. Các số nguyên tố trong tuple: {nguyen_to}")
    return nguyen_to
def bai6_tong_cac_so(tup):
    tong = sum(tup)
    print(f"6. Tổng các số trong tuple: {tong}")
    return tong


def main():
    print("--- CHƯƠNG TRÌNH XỬ LÝ TUPLE (ĐỀ 6) ---\n")
    

    my_tuple = bai1_nhap_tuple()
    print(f"   Tuple vừa nhập hợp lệ: {my_tuple}\n")
        

    bai2_trung_binh_cong(my_tuple)
    

    bai6_tong_cac_so(my_tuple)

    bai4_so_hoan_hao(my_tuple)

    bai5_so_nguyen_to(my_tuple)
    

    my_tuple = bai3_chen_x(my_tuple)

if __name__ == "__main__":
    main()