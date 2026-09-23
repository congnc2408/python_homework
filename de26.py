from collections import Counter
def bai1_nhap_va_dao_xau():
    s = input("1. Nhập xâu ký tự s: ")
    xau_dao = s[::-1]
    print(f"   => Xâu đảo của xâu vừa nhập là: '{xau_dao}'")
    return s, xau_dao

def bai2_hien_thi_xau_con(s):
    n = len(s)
    xau_con = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            xau_con.append(s[i:j])
    print(f"2. Các xâu con của xâu s ({len(xau_con)} xâu): {xau_con}")
    return xau_con

def bai3_ky_tu_nhieu_nhat(s):
    if not s:
        print("3. Xâu rỗng.")
        return []
    dem = Counter(s)
    max_count = max(dem.values())
    ket_qua = [k for k, v in dem.items() if v == max_count]
    print(f"3. (Các) ký tự xuất hiện nhiều nhất (số lần: {max_count}): {ket_qua}")
    return ket_qua

def bai4_xoa_ky_tu_trung(s):
    ket_qua = "".join(dict.fromkeys(s))
    print(f"4. Xâu sau khi xóa các ký tự trùng nhau: '{ket_qua}'")
    return ket_qua

def bai5_dem_chi_tiet(s):
    # Tập hợp các nguyên âm (bao gồm cả tiếng Anh và tiếng Việt có dấu cơ bản)
    nguyen_am_set = "ueoaiüöäaeiouáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵAEIOUUEOAIÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬÉÈẺẼẸÊẾỀỂỄỆÍÌỈĨỊÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÚÙỦŨỤƯỨỪỬỮỰÝỲỶỸỴ"
    
    so_nguyen_am = sum(1 for c in s if c in nguyen_am_set)
    so_khoang_trang = sum(1 for c in s if c.isspace())
    so_phu_am = sum(1 for c in s if c.isalpha() and c not in nguyen_am_set)
    
    print(f"5. Thống kê trong xâu:")
    print(f"   - Số nguyên âm: {so_nguyen_am}")
    print(f"   - Số phụ âm: {so_phu_am}")
    print(f"   - Số khoảng trắng: {so_khoang_trang}")
    return so_nguyen_am, so_phu_am, so_khoang_trang

def bai6_la_so_nguyen_duong(s):
    la_so = s.isdigit() and int(s) > 0
    if la_so:
        print(f"6. Xâu '{s}' CÓ biểu diễn một số nguyên dương.")
    else:
        print(f"6. Xâu '{s}' KHÔNG biểu diễn một số nguyên dương.")
    return la_so

def bai7_xoa_ky_tu_x(s):
    x = input("7. Nhập ký tự X cần xóa: ")
    ket_qua = s.replace(x, "")
    print(f"   => Xâu sau khi xóa ký tự '{x}': '{ket_qua}'")
    return ket_qua

def main():
    print("--- CHƯƠNG TRÌNH XỬ LÝ XÂU KÝ TỰ (ĐỀ 26) ---\n")

    s, _ = bai1_nhap_va_dao_xau()
    print()
    
    if not s:
        print("Xâu rỗng. Kết thúc chương trình.")
        return

    bai2_hien_thi_xau_con(s)
    print()
    
    bai3_ky_tu_nhieu_nhat(s)
    print()
    

    bai4_xoa_ky_tu_trung(s)
    print()
    
    bai5_dem_chi_tiet(s)
    print()
    
    bai6_la_so_nguyen_duong(s)
    print()
    
    bai7_xoa_ky_tu_x(s)

if __name__ == "__main__":
    main()