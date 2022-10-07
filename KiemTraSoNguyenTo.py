
#hàm kiểm tra số nguyên tố
def SoNguyenTo (n):
    if(n<2):
        return 0;
    for i in range(2,n):
        if(n%i==0):
            return 0;
    return 1;
#nhap số từ bàn phím
so= int(input('nhập số kiểm tra: '))
checkNT = SoNguyenTo(so)
if(checkNT == 0):
    print('số %i đã nhập không phải là số nguyên tố!!'%so)
else: 
    print('sô %i đã cho là số nguyên tố!!'%so)