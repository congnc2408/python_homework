

from collections import Counter
def bai1_nhap_va_in():
    s = input("Nhập xâu ký tự s: ")
    print(f"Các ký tự  trong xâu vừa nhập:  {list(s)}")
    return s

def bai2_xau_dao_nguoc(s):
    return s[::-1]

def bai3_dem_xau_con(s,s1):
    return s.count(s1)

def bai4_kiem_tra_bat_dau(s,s2):
    return s.startswith(s2)

def bai5_16_ky_tu_xuat_hien_it_nhat(s):
    if not s:
        return []
    dem = Counter(s)
    min_count = min(dem.values())
    ket_qua = [k for k, v in dem.items() if v == min_count]
    ket_qua.sort()
    return ket_qua

def bai6_bat_dau_chu_hoa(s):
    if not s:
        return False
    return s[0].isupper()

def bai7_cac_xau_con(s):
    n = len(s)
    xau_con = []
    for i in range(n):
        for j in range(i+1, n+1):
            xau_con.append(s[i:j])
    return xau_con

def bai8_dem_hoa_thuong(s):
    hoa = sum(1 for c in s if c.isupper())
    thuong = sum(1 for c in s if c.islower())
    return hoa,thuong    

def bai9_sap_xep_tang_dan(s):
    return "".join(sorted(s))

def bai10_kiem_tra_ket_thuc(s, s1):
    return s.endswith(s1)
def bai11_ky_tu_xuat_hien_nhieu_nhat(s):
    if not s: 
        return []
    dem = Counter(s)
    max_count = max(dem.values())
    return [k for k,v in dem.items() if v == max_count]

def bai12_kiem_tra_tu_bat_dau_hoa(s):
    tu_list = s.split()
    if not tu_list:
        return False
    return all(tu[0].isupper() for tu in tu_list)

def bai13_tach_va_in_tu(s):
    tu_list = s.split()
    for tu in tu_list:
        print(tu)

def bai14_xoa_tu_cuoi(s):
    tu_list = s.split()
    if not tu_list:
        return s
    return " ".join(tu_list[:-1])

def bai15_19_dem_so_tu(s):
    return len(s.split())

def bai17_kiem_tra_s1_la_dao_nguoc(s,s1):
    return s[::-1] == s1
def bai18_kiem_tra_doi_xung(s):
    return s == s[::-1]

def bai20_xoa_chu_so(s):
    return "".join(x for x in s if not x.isdigit())

def bai21_tu_ngan_nhat(s):
    tu_list =  s.split()
    if not tu_list:
        return ""
    return min(tu_list, key=len)

def bai22_dem_chu_cai(s):
    return sum(1 for c in s if c.isalpha())

def bai23_kiem_tra_toan_hoa(s):
    return s.isupper() if s else False

def main():

    print("--- CHƯƠNG TRÌNH KIỂM THỬ XÂU KÝ TỰ (ĐỀ 3) ---\n")
    s = bai1_nhap_va_in()

    print(f"2. Xâu đảo ngược: '{bai2_xau_dao_nguoc(s)}'")
    s1 = input("\nNhập xâu con s1 (cho câu 3 và 10): ")
    print(f"3. Số lần s1 xuất hiện trong s: {bai3_dem_xau_con(s, s1)}")
    print(f"10. Xâu s có kết thúc bằng s1 không? {bai10_kiem_tra_ket_thuc(s, s1)}")
    s2 = input("Nhập xâu con s2 (cho câu 4): ")
    print(f"4. Xâu s có bắt đầu bằng s2 không? {bai4_kiem_tra_bat_dau(s, s2)}")
    print(f"\n5 & 16. (Các) Ký tự xuất hiện ít nhất: {bai5_16_ky_tu_xuat_hien_it_nhat(s)}")
    print(f"6. Xâu s có bắt đầu bằng chữ hoa không? {bai6_bat_dau_chu_hoa(s)}")
    print(f"7. Tất cả các xâu con: {bai7_cac_xau_con(s)}")
    hoa, thuong = bai8_dem_hoa_thuong(s)
    print(f"8. Số chữ hoa: {hoa}, Số chữ thường: {thuong}")
    print(f"9. Xâu sau khi sắp xếp tăng dần: '{bai9_sap_xep_tang_dan(s)}'")
    print(f"11. (Các) Ký tự xuất hiện nhiều nhất: {bai11_ky_tu_xuat_hien_nhieu_nhat(s)}")
    print(f"12. Tất cả các từ đều bắt đầu bằng chữ hoa? {bai12_kiem_tra_tu_bat_dau_hoa(s)}")
    print("13. Tách xâu và in từng từ:")
    bai13_tach_va_in_tu(s)
    print(f"14. Xâu sau khi xóa từ cuối cùng: '{bai14_xoa_tu_cuoi(s)}'")
    print(f"15 & 19. Số lượng từ trong xâu: {bai15_19_dem_so_tu(s)}")
    s1_check = input("\nNhập xâu s1 (để kiểm tra xem có phải đảo ngược của s ở câu 17 không): ") 
    print(f"17. s1 có phải là đảo ngược của s không? {bai17_kiem_tra_s1_la_dao_nguoc(s, s1_check)}")
    print(f"18. Xâu s có phải là chuỗi đối xứng không? {bai18_kiem_tra_doi_xung(s)}")
    print(f"20. Xâu sau khi xóa các chữ số: '{bai20_xoa_chu_so(s)}'")
    print(f"21. Từ ngắn nhất: '{bai21_tu_ngan_nhat(s)}'")
    print(f"22. Số lượng chữ cái trong xâu: {bai22_dem_chu_cai(s)}")
    print(f"23. Xâu s có phải là toàn chữ hoa không? {bai23_kiem_tra_toan_hoa(s)}")
    return

if __name__ == "__main__":
    main()