


def bai1_nhap_va_in():
    s = input("Nhập xâu ký tự s: ")
    print(f"Các ký tự trong xâu vừa nhập: {list(s)}")
    return s

def  bai2_demso(s):
    return  sum(1 for c in s if c.isdigit())

def bai3_19_tu_dai_nhat(s):
    tu_list = s.split()
    if not tu_list:
        return ""
    return max(tu_list, key=len)

def bai4_kiem_tra_xau_con(s,s1):
    return s1 in s

def bai5_xau_con_khac_nhau(s):
    xau_con = set()
    n = len(s)
    for i in range(n):
        for j in range(i+1, n+1):
            xau_con.add(s[i:j])
    return xau_con

def bai6__20_xoa_tu_dau(s):
    tu_list = s.split()
    if not  tu_list:
        return s
    return " ".join(tu_list[1:])

def bai7_chuyen_thanh_ascii(s):
    return [ord(c) for c in s]

def bai8_ky_tu_ma_lon_nhat(s):
    if not s: 
        return None
    return max(s)

def bai9_sap_xep_tu_theo_do_dai(s):
    tu_list = s.split()
    return sorted(tu_list, key=len)


def bai10_dem_ky_tu_dac_biet(s):
    return sum(1 for c in s if not c.isalnum())


def bai11_xau_con_dai_nhat_chua_tat_ca_ky_tu(s):
    return s

def bai12_kiem_tra_ky_tu(s,c):
    return c in s

def bai13_loai_bo_khoang_trang_dau_cuoi(s):
    return s.strip()

def bai14_vi_tri_xuat_hien_xau_con(s,s1):
    vi_tri = []
    if not s1:
        return vi_tri
    start = 0
    while True:
        start = s.find(s1,start)
        if start == -1:
            break
        vi_tri.append(start)
        start +=1
    return vi_tri

def bai15_dem_chu_hia(s):
    return  sum(1 for c in s if c.isupper())


def bai16_viet_hoa_chu_dau(s):
    return s.title()

def bai17_vi_tri_ky_tu(s,c):
    return [i for i, char in enumerate(s) if char == c]

def bai18_chi_giu_chu_va_so(s):
    return  "".join(c for c in s if c.isalnum())

def bai21_gep_chuoi(s1, s2):
    return s1 + s2

def main():
   print("--- CHƯƠNG TRÌNH KIỂM THỬ XÂU KÝ TỰ (ĐỀ 4) ---\n")
   s = bai1_nhap_va_in()
   print(f"2. Số lượng ký tự số trong xâu: {bai2_dem_so(s)}")
   s1 = input("\nNhập xâu s1 (cho câu 4, 14, 21): ")
   print(f"4. s1 có phải xâu con của s không? {bai4_kiem_tra_xau_con(s, s1)}")
   ds_xau_con = bai5_xau_con_khac_nhau(s)
   print(f"5. Số lượng xâu con khác nhau được tìm thấy: {len(ds_xau_con)}")
   print(f"6 & 20. Xâu sau khi xóa từ đầu tiên: '{bai6_20_xoa_tu_dau(s)}'")
   print(f"7. Mã ASCII của xâu: {bai7_chuyen_thanh_ascii(s)}")
   print(f"8. Ký tự có mã ASCII lớn nhất: '{bai8_ky_tu_ma_lon_nhat(s)}'")
   print(f"9. Danh sách từ sắp xếp độ dài tăng dần: {bai9_sap_xep_tu_theo_do_dai(s)}")
   print(f"10. Số lượng ký tự đặc biệt (bao gồm dấu cách): {bai10_dem_ky_tu_dac_biet(s)}")
   print(f"11. Xâu con dài nhất chứa tất cả ký tự của s: '{bai11_xau_con_dai_nhat_chua_tat_ca_ky_tu(s)}'")
   c = input("\nNhập ký tự C (cho câu 12, 17): ")
   print(f"12. Ký tự '{c}' có trong xâu không? {bai12_kiem_tra_ky_tu(s, c)}")
   print(f"17. Các vị trí xuất hiện của '{c}': {bai17_vi_tri_ky_tu(s, c)}")
   print(f"13. Xâu sau khi loại khoảng trắng 2 đầu: '{bai13_loai_bo_khoang_trang_dau_cuoi(s)}'")
   print(f"14. Các vị trí xuất hiện của s1 trong s: {bai14_vi_tri_xuat_hien_xau_con(s, s1)}")
   print(f"15. Số lượng chữ hoa trong xâu: {bai15_dem_chu_hoa(s)}")
   print(f"16. Viết hoa chữ đầu mỗi từ: '{bai16_viet_hoa_chu_dau(s)}'")
   print(f"18. Chỉ giữ lại chữ cái và số (không có dấu cách): '{bai18_chi_giu_chu_va_so(s)}'")
   print(f"21. Ghép s và s1 thành: '{bai21_ghep_chuoi(s, s1)}'")
    
if __name__ == "__main__":
    main()