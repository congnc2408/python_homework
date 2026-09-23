
def bai1_nhap_danh_sach():
    while True:
        chuoi = input("1. Nhập dãy số nguyên, cách nhau bằng dấu phẩy: ")
        try:
            lst = [int(x.strip()) for x in chuoi.split(',')]
            return lst
        except ValueError:
            print("   -> Lỗi: Dữ liệu nhập vào không hợp lệ, vui lòng chỉ nhập số nguyên.")

def bai2_in_chan_le(lst):
    chan = [x for x in lst if x % 2 == 0]
    le = [x for x in lst if x % 2 != 0]
    print(f"2. Các số chẵn: {chan}")
    print(f"   Các số lẻ: {le}")
    return chan, le

def bai3_so_am_lien_tiep_min(lst):
    cac_doan_am = []
    do_dai_hien_tai = 0
    
    for x in lst:
        if x < 0:
            do_dai_hien_tai += 1
        else:
            if do_dai_hien_tai > 0:
                cac_doan_am.append(do_dai_hien_tai)
                do_dai_hien_tai = 0
                
    if do_dai_hien_tai > 0:
        cac_doan_am.append(do_dai_hien_tai)

    if not cac_doan_am:
        min_len = 0
    else:
        min_len = min(cac_doan_am)
        
    print(f"3. Số lượng các số âm liên tiếp ít nhất là: {min_len}")
    return min_len


def bai4_tong_va_trung_binh(lst):
    if not lst:
        print("4. Danh sách rỗng (Tổng: 0, Trung bình: 0)")
        return 0, 0
    tong = sum(lst)
    tbc = tong / len(lst)
    print(f"4. Tổng các phần tử: {tong}")
    print(f"   Trung bình cộng: {tbc}")
    return tong, tbc

def main():
    print("--- CHƯƠNG TRÌNH XỬ LÝ DANH SÁCH (ĐỀ 14) ---\n")
    
    danh_sach = bai1_nhap_danh_sach()
    print(f"\n=> Danh sách vừa nhập: {danh_sach}\n")
    
    if not danh_sach:
        print("Danh sách trống, kết thúc chương trình.")
        return

    bai2_in_chan_le(danh_sach)
    print()
    

    bai3_so_am_lien_tiep_min(danh_sach)
    print()
    
    bai4_tong_va_trung_binh(danh_sach)

if __name__ == "__main__":
    main()
