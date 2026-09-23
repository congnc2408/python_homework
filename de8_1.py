def bai1_nhap_thong_tin():
    myclass = {}
    print("--- Nhập thông tin học sinh (Nhập 'q' ở tên để dừng) ---")
    while True:
        ten = input("Nhập tên học sinh: ")
        if ten.lower() == 'q':
            break
        
        while True:
            try:
                diem = int(input(f"Nhập điểm cho {ten} (0,1,2,...,10): "))
               
                if 0 <= diem <= 10:
                    break
                else:
                    print("   -> Lỗi: Điểm phải là số nguyên từ 0 đến 10. Vui lòng nhập lại.")
            except ValueError:
                print("   -> Lỗi: Vui lòng nhập một số nguyên hợp lệ.")
                
        myclass[ten] = diem
    return myclass


def bai2_thong_ke_diem(myclass):
    thong_ke = {}
    for diem in myclass.values():
        if diem in thong_ke:
            thong_ke[diem] += 1
        else:
            thong_ke[diem] = 1
            
    print("2. Thống kê điểm số:")
    
    for diem in sorted(thong_ke.keys(), reverse=True):
        print(f"   - Điểm {diem}: {thong_ke[diem]} học sinh")
    return thong_ke
def bai3_dem_hoc_sinh_gioi(myclass):
    dem = sum(1 for diem in myclass.values() if diem >= 7)
    print(f"3. Số học sinh có điểm giỏi (>= 7): {dem} học sinh")
    return dem

def bai4_xoa_hoc_sinh(myclass, ten_can_xoa="Huệ Chi"):

    if ten_can_xoa in myclass:
        del myclass[ten_can_xoa]
        print(f"4. Đã xóa học sinh '{ten_can_xoa}' khỏi danh sách lớp.")
    else:
        print(f"4. Không tìm thấy học sinh '{ten_can_xoa}' trong danh sách để xóa.")
    return myclass


def main():
    print("--- CHƯƠNG TRÌNH QUẢN LÝ LỚP HỌC (ĐỀ 8) ---\n")
    
    
    myclass = bai1_nhap_thong_tin()
    print(f"\n=> Danh sách lớp (myclass) hiện tại: {myclass}\n")
    
    if not myclass:
        print("Lớp học chưa có dữ liệu.")
        return

    bai2_thong_ke_diem(myclass)
    print()
    

    bai3_dem_hoc_sinh_gioi(myclass)
    print()

    myclass = bai4_xoa_hoc_sinh(myclass, "Huệ Chi")
    print(f"=> Danh sách lớp sau khi xóa: {myclass}")

if __name__ == "__main__":
    main()