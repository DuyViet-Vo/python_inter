#hàm kiểm tra số nguyên tố
def SoNguyenTo (n):
    if(n<2):
        return n;
    for i in range(2,n):
        if(n%i==0):
            return False;
    return n;
for i in range(1,100):
    sd = ''
    sd = sd + str(SoNguyenTo(i));
    print(sd,end=",")
  