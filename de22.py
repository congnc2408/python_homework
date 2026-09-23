
def bai1_nhap_tu_vung():
    chuoi = input("1. Nhập chuỗi các từ vựng, cách nhau bằng dấu phẩy: ")
    ds_tu = [tu.strip() for tu in chuoi.split(',') if tu.strip()]
    print(f"   => Danh sách từ vựng vừa nhập: {ds_tu}")
    return ds_tu

def bai2_sap_xep_alphabet(ds_tu):
    ds_sap_xep = sorted(ds_tu)
    print(f"2. Danh sách từ vựng sắp xếp theo bảng chữ cái: {ds_sap_xep}")
    return ds_sap_xep

def bai3_loai_bo_trung(ds_tu):
    ds_khong_trung = list(dict.fromkeys(ds_tu))
    print(f"3. Danh sách sau khi loại bỏ các từ trùng lặp: {ds_khong_trung}")
    return ds_khong_trung

def bai4_dem_tu_chua_so(ds_tu):
    tu_chua_so = [tu for tu in ds_tu if any(c.isdigit() for c in tu)]
    so_luong = len(tu_chua_so)
    print(f"4. Số lượng các từ có chứa chữ số: {so_luong} (gồm: {tu_chua_so})")
    return so_luong

def main():
    print("--- CHƯƠNG TRÌNH QUẢN LÝ TỪ VỰNG (ĐỀ 22) ---\n")

    danh_sach_tu = bai1_nhap_tu_vung()
    print()
    
    if not danh_sach_tu:
        print("Danh sách từ vựng trống. Kết thúc chương trình.")
        return

    bai2_sap_xep_alphabet(danh_sach_tu)
    print()
    

    bai3_loai_bo_trung(danh_sach_tu)
    print()
    
    bai4_dem_tu_chua_so(danh_sach_tu)

if __name__ == "__main__":
    main()