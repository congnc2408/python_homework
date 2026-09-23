
def bai1_nhap_va_in_ky_tu():
    s = input("1. Nhập một chuỗi ký tự s: ")
    print(f"   => Các ký tự trong chuỗi vừa nhập: {list(s)}")
    return s

def bai2_do_dai_tu_dai_nhat(s):
    tu_list = s.split()
    if not tu_list:
        print("2. Chuỗi trống, không có từ nào.")
        return 0
    max_len = max(len(tu) for tu in tu_list)
    print(f"2. Độ dài từ dài nhất trong chuỗi là: {max_len}")
    return max_len

def bai3_kiem_tra_va_loc_chuoi_so(s):
    la_so = s.isdigit()
    if la_so:
        print(f"3. Chuỗi '{s}' CÓ phải là chuỗi số.")
        ket_qua = s
    else:
        ket_qua = "".join(c for c in s if c.isdigit())
        print(f"3. Chuỗi '{s}' KHÔNG phải là chuỗi số.")
        print(f"   => Sau khi xóa các ký tự không phải số: '{ket_qua}'")
    return ket_qua

def bai4_kiem_tra_chu_thuong(s):
    la_thuong = s.islower()
    if la_thuong:
        print(f"4. Chuỗi '{s}' toàn bộ là chữ thường.")
    else:
        print(f"4. Chuỗi '{s}' KHÔNG phải toàn bộ là chữ thường.")
    return la_thuong

def main():
    print("--- CHƯƠNG TRÌNH XỬ LÝ XÂU KÝ TỰ (ĐỀ 28) ---\n")

    s = bai1_nhap_va_in_ky_tu()
    print()
    
    if not s:
        print("Chuỗi rỗng. Kết thúc chương trình.")
        return

    bai2_do_dai_tu_dai_nhat(s)
    print()
    
    bai3_kiem_tra_va_loc_chuoi_so(s)
    print()
    
    bai4_kiem_tra_chu_thuong(s)

if __name__ == "__main__":
    main()