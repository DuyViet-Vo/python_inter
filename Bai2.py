n = int(input('Nhập số tính giai thừa: '))
#hàm tính giai thưa
def tinhGiaiThua(n):
    if n==0:
        return 1;
    return n*tinhGiaiThua(n-1)
print(tinhGiaiThua(n))
