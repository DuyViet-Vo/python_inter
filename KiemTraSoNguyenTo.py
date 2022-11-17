
#hàm kiểm tra số nguyên tố
def SoNguyenTo (n):
    if(n<2):
        return False;
    for i in range(2,abs(n)):
        if(n%i==0):
            return False;
    return True;
#nhap số từ bàn phím
so= int(input('nhập số kiểm tra: '))
if(SoNguyenTo(so)):
    print('số %i đã cho là số nguyên tố!!'%so)
else: 
    print('số %i đã nhập không phải là số nguyên tố!!'%so)