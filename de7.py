
def bai1_nhap_xau():
    return input("Nhập xâu ký tự s: ")


def bai2_loai_bo_trung(s):
    ket_qua = ""
    for c in s:
        if c not in ket_qua:
            ket_qua += c
    return ket_qua


def bai3_in_xau_con(s):
    n = len(s)
    xau_con = []
   
    for i in range(n):
        for j in range(i + 1, n + 1):
            xau_con.append(s[i:j])
            
    print(f"Các xâu con của s ({len(xau_con)} xâu): {xau_con}")
    return xau_con


def bai4_xau_con_dai_nhat_khong_trung(s):
    
    vi_tri_ky_tu = {}
    bat_dau = 0
    do_dai_max = 0
    xau_con_max = ""
    
    for i, ky_tu in enumerate(s):

        if ky_tu in vi_tri_ky_tu and vi_tri_ky_tu[ky_tu] >= bat_dau:
            bat_dau = vi_tri_ky_tu[ky_tu] + 1

        vi_tri_ky_tu[ky_tu] = i
        

        do_dai_hien_tai = i - bat_dau + 1
        if do_dai_hien_tai > do_dai_max:
            do_dai_max = do_dai_hien_tai
            xau_con_max = s[bat_dau:i+1]
            
    return xau_con_max


def main():
    print("--- CHƯƠNG TRÌNH XỬ LÝ XÂU KÝ TỰ (ĐỀ 7) ---\n")

    s = bai1_nhap_xau()
    

    print(f"\n2. Xâu sau khi loại bỏ ký tự trùng lặp: '{bai2_loai_bo_trung(s)}'")

    print("\n3.", end=" ")
    bai3_in_xau_con(s)

    print(f"\n4. Xâu con dài nhất không chứa ký tự trùng lặp: '{bai4_xau_con_dai_nhat_khong_trung(s)}'")

if __name__ == "__main__":
    main()