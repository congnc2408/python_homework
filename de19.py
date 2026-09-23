
def bai1_nhap_danh_ba():
    danh_ba = {}
    print("--- 1. Nhập danh bạ (Nhập 'q' ở phần Tên để dừng) ---")
    while True:
        ten = input("Nhập tên người dùng: ").strip()
        if ten.lower() == 'q':
            break
        sdt = input(f"Nhập số điện thoại của {ten}: ").strip()
        danh_ba[ten] = sdt
    return danh_ba

def bai2_xoa_hoa(danh_ba):
    danh_ba_moi = danh_ba.copy()
    keys_to_delete = [ten for ten in danh_ba_moi.keys() if ten.lower() == "hoa"]
    
    if keys_to_delete:
        for ten in keys_to_delete:
            del danh_ba_moi[ten]
        print(f"2. Đã xóa thông tin của người có tên 'Hoa' khỏi danh sách[cite: 21].")
    else:
        print(f"2. Không tìm thấy người nào có tên 'Hoa' trong danh bạ[cite: 21].")
        
    print(f"   Danh sách sau khi xóa: {danh_ba_moi}")
    return danh_ba_moi

def bai3_tim_ten_theo_sdt(danh_ba):
    sdt_can_tim = input("\n3. Nhập số điện thoại cần tìm tên: ").strip()
    nguoi_tim_thay = [ten for ten, sdt in danh_ba.items() if sdt == sdt_can_tim]
    
    if nguoi_tim_thay:
        print(f"   => Tên người dùng có số điện thoại {sdt_can_tim} là: {', '.join(nguoi_tim_thay)}")
    else:
        print(f"   => Không tìm thấy người dùng nào có số điện thoại {sdt_can_tim}.")
    return nguoi_tim_thay

def bai4_chen_thong_tin(danh_ba):
    danh_ba_moi = danh_ba.copy()
    print("\n4. Chèn thông tin người mới vào danh bạ:")
    ten_moi = input("   - Nhập tên: ").strip()
    sdt_moi = input(f"   - Nhập số điện thoại của {ten_moi}: ").strip()
    danh_ba_moi[ten_moi] = sdt_moi
    print(f"   => Đã chèn thành công '{ten_moi}: {sdt_moi}' vào danh bạ.")
    print(f"   Danh sách sau khi chèn: {danh_ba_moi}")
    return danh_ba_moi

def main():
    print("--- CHƯƠNG TRÌNH QUẢN LÝ DANH BẠ (ĐỀ 19) ---\n")
    
    danh_ba = bai1_nhap_danh_ba()
    print(f"\n=> Danh sách danh bạ ban đầu: {danh_ba}\n")
    
    if not danh_ba:
        print("Danh sách trống. Kết thúc chương trình.")
        return

    danh_ba = bai2_xoa_hoa(danh_ba)
    
    bai3_tim_ten_theo_sdt(danh_ba)
    
    danh_ba = bai4_chen_thong_tin(danh_ba)

if __name__ == "__main__":
    main()