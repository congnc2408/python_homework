def bai1_nhap_danh_ba():
    danh_ba = {}
    print("--- Nhập danh bạ (Nhập 'q' ở phần Tên để dừng) ---")
    while True:
        ten = input("Nhập họ tên người dùng: ")
        if ten.lower() == 'q':
            break
        sdt = input(f"Nhập số điện thoại của {ten}: ")
        danh_ba[ten] = sdt
    return danh_ba

def bai2_hien_thi_z_den_a(danh_ba):
    print("\n2. Danh bạ sắp xếp từ Z đến A theo họ tên:")
    if not danh_ba:
        print("   -> Danh bạ trống.")
        return
    
    
    for ten in sorted(danh_ba.keys(), reverse=True):
        print(f"   - {ten}: {danh_ba[ten]}")

def bai3_tim_theo_ten(danh_ba):
    xau_tim_kiem = input("\n3. Nhập xâu ký tự cần tìm trong họ tên: ")
    
    ket_qua = {ten: sdt for ten, sdt in danh_ba.items() if xau_tim_kiem.lower() in ten.lower()}
    
    if ket_qua:
        print(f"   => Tìm thấy {len(ket_qua)} liên hệ phù hợp:")
        for ten, sdt in ket_qua.items():
            print(f"      - {ten}: {sdt}")
    else:
        print(f"   => Không tìm thấy ai có họ tên chứa '{xau_tim_kiem}'.")
    return ket_qua


def bai4_tim_theo_sdt(danh_ba):
    sdt_tim_kiem = input("\n4. Nhập số điện thoại cần tìm: ")
    nguoi_tim_thay = [ten for ten, sdt in danh_ba.items() if sdt == sdt_tim_kiem]
    
    if nguoi_tim_thay:
        
        print(f"   => Tên của người có số điện thoại {sdt_tim_kiem} là: {', '.join(nguoi_tim_thay)}")
    else:
        print(f"   => Không tìm thấy liên hệ nào sử dụng số điện thoại {sdt_tim_kiem}.")
    return nguoi_tim_thay



def main():
    print("--- CHƯƠNG TRÌNH QUẢN LÝ DANH BẠ (ĐỀ 9) ---\n")
    

    danh_ba_cua_toi = bai1_nhap_danh_ba()
    
    if not danh_ba_cua_toi:
        print("\nDanh bạ trống. Kết thúc chương trình.")
        return

    bai2_hien_thi_z_den_a(danh_ba_cua_toi)

    bai3_tim_theo_ten(danh_ba_cua_toi)
    
    bai4_tim_theo_sdt(danh_ba_cua_toi)

if __name__ == "__main__":
    main()