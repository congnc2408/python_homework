
def bai1_nhap_ten_sach():
    chuoi = input("1. Nhập chuỗi tên các cuốn sách, cách nhau bằng dấu phẩy: ")
    ds_sach = [sach.strip() for sach in chuoi.split(',') if sach.strip()]
    print(f"   => Danh sách tên sách vừa nhập: {ds_sach}")
    return ds_sach

def bai2_sap_xep_alphabet(ds_sach):
    ds_sap_xep = sorted(ds_sach)
    print(f"2. Danh sách tên sách sắp xếp theo bảng chữ cái: {ds_sap_xep}")
    return ds_sap_xep


def bai3_xoa_sach_trung(ds_sach):
    ds_khong_trung = list(dict.fromkeys(ds_sach))
    print(f"3. Danh sách sau khi xóa các tên sách trùng nhau: {ds_khong_trung}")
    return ds_khong_trung

def bai4_ten_sach_dai_nhat(ds_sach):
    if not ds_sach:
        print("4. Danh sách trống.")
        return []
    max_len = len(max(ds_sach, key=len))
    ds_dai_nhat = [sach for sach in ds_sach if len(sach) == max_len]
    print(f"4. Tên sách dài nhất ({max_len} ký tự): {', '.join(ds_dai_nhat)}")
    return ds_dai_nhat

def main():
    print("--- CHƯƠNG TRÌNH QUẢN LÝ THƯ VIỆN (ĐỀ 23) ---\n")

    danh_sach_sach = bai1_nhap_ten_sach()
    print()
    
    if not danh_sach_sach:
        print("Danh sách thư viện trống. Kết thúc chương trình.")
        return

    bai2_sap_xep_alphabet(danh_sach_sach)
    print()
    
    bai3_xoa_sach_trung(danh_sach_sach)
    print()
    
    bai4_ten_sach_dai_nhat(danh_sach_sach)

if __name__ == "__main__":
    main()