import os

def tao_ma_tran_playfair(khoa):
    khoa = khoa.replace(" ", "").upper()
    khoa = khoa.replace("J", "I")  # Thay thế 'J' bằng 'I'
    bang_chu_cai = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    ma_tran = []

    # Điền ma trận với khóa
    for ki_tu in khoa:
        if ki_tu not in ma_tran:
            ma_tran.append(ki_tu)

    # Điền phần còn lại của ma trận với bảng chữ cái
    for ki_tu in bang_chu_cai:
        if ki_tu not in ma_tran and ki_tu != 'J':  # Loại trừ 'J' vì đã thay thế bằng 'I'
            ma_tran.append(ki_tu)

    # Chuyển ma trận thành lưới 5x5
    ma_tran_playfair = [ma_tran[i:i+5] for i in range(0, 25, 5)]
    return ma_tran_playfair

def tim_vi_tri(ma_tran, ki_tu):
    for i in range(5):
        for j in range(5):
            if ma_tran[i][j] == ki_tu:
                return i, j

def ma_hoa_playfair(van_ban_ro, khoa):
    ma_tran_playfair = tao_ma_tran_playfair(khoa)
    van_ban_ro = van_ban_ro.upper().replace(" ", "")
    van_ban_ma_hoa = ""

    # Thêm 'X' vào giữa các cặp ký tự giống nhau nằm cạnh nhau
    i = 0
    while i < len(van_ban_ro) - 1:
        ki_tu1 = van_ban_ro[i]
        ki_tu2 = van_ban_ro[i+1]

        if ki_tu1 == ki_tu2:
            van_ban_ro = van_ban_ro[:i+1] + 'X' + van_ban_ro[i+1:]
        i += 2
    if len(van_ban_ro) % 2 != 0:  # Nếu chiều dài của văn bản là số lẻ, thêm 'X' vào cuối
        van_ban_ro += 'X'

    # Mã hóa văn bản
    for i in range(0, len(van_ban_ro), 2):
        ki_tu1 = van_ban_ro[i]
        ki_tu2 = van_ban_ro[i+1]

        hang1, cot1 = tim_vi_tri(ma_tran_playfair, ki_tu1)
        hang2, cot2 = tim_vi_tri(ma_tran_playfair, ki_tu2)

        if hang1 == hang2:  # Cùng hàng
            van_ban_ma_hoa += ma_tran_playfair[hang1][(cot1 + 1) % 5]
            van_ban_ma_hoa += ma_tran_playfair[hang2][(cot2 + 1) % 5]
        elif cot1 == cot2:  # Cùng cột
            van_ban_ma_hoa += ma_tran_playfair[(hang1 + 1) % 5][cot1]
            van_ban_ma_hoa += ma_tran_playfair[(hang2 + 1) % 5][cot2]
        else:  # Khác hàng và cột
            van_ban_ma_hoa += ma_tran_playfair[hang1][cot2]
            van_ban_ma_hoa += ma_tran_playfair[hang2][cot1]

    return van_ban_ma_hoa


def chuong_trinh_chinh():
    khoa = input("Nhập khóa (chữ không có dấu và không chứa 'J'): ")
    van_ban_ro = input("Nhập văn bản cần mã hóa: ")
    van_ban_ma_hoa = ma_hoa_playfair(van_ban_ro, khoa)
    print("Văn bản đã mã hóa:", van_ban_ma_hoa)

if __name__ == "__main__":
    chuong_trinh_chinh()
