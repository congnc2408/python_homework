def bai1_nhap_danh_ba():
    danh_ba = {}
    so_luong = 15
    print(f"--- 1. Nhập danh bạ ({so_luong} người dùng) ---")
    for i in range(1, so_luong + 1):
        ten = input(f"Nhập tên người dùng thứ {i}: ")
        sdt = input(f"Nhập số điện thoại của {ten}: ")
        danh_ba[ten] = sdt
        
    return danh_ba

def bai2_hien_thi_tong_so(danh_ba):
    tong_so = len(danh_ba)
    print(f"\n2. Tổng số người có trong danh bạ hiện tại là: {tong_so}")
    return tong_so

def bai3_tim_sdt_theo_ten(danh_ba):
    ten_tim_kiem = input("\n3. Nhập tên cần tìm số điện thoại: ")

    if ten_tim_kiem in danh_ba:
        print(f"   => Số điện thoại của '{ten_tim_kiem}' là: {danh_ba[ten_tim_kiem]}")
    else:
        print(f"   => Không tìm thấy người dùng tên '{ten_tim_kiem}' trong danh bạ.")

def bai4_tim_nguoi_theo_chuoi_so(danh_ba):
    chuoi_so = input("\n4. Nhập chuỗi số điện thoại cần tìm: ")

    ket_qua = {ten: sdt for ten, sdt in danh_ba.items() if chuoi_so in sdt}
    
    if ket_qua:
        print(f"   => Có {len(ket_qua)} người có số điện thoại chứa chuỗi '{chuoi_so}':")
        for ten, sdt in ket_qua.items():
            print(f"      - {ten}: {sdt}")
    else:
        print(f"   => Không tìm thấy ai có số điện thoại chứa chuỗi '{chuoi_so}'.")
    return ket_qua

def main():
    print("--- CHƯƠNG TRÌNH QUẢN LÝ DANH BẠ (ĐỀ 10) ---\n")
    
    danh_ba_cua_toi = bai1_nhap_danh_ba()

    bai2_hien_thi_tong_so(danh_ba_cua_toi)

    bai3_tim_sdt_theo_ten(danh_ba_cua_toi)

    bai4_tim_nguoi_theo_chuoi_so(danh_ba_cua_toi)

if __name__ == "__main__":
    main()