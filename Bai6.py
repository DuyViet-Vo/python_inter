import math
def isNguyenTo(n):
    if(n<2):
        return False;
    v = int(math.sqrt(n));
    for i in range(2,v+1):
        if(n%i==0):
            return False;
        return True;

n = int(input('nhap gia trị n: '))
print('tất cả số nguyên tố nhỏ hơn ',n,'là: ')
sb =""
if(n>=2):
    sb= sb +'2'+''
for i in range(3, n+1):
    if(isNguyenTo(i)):
        sb = sb + str(i)+ " ";
    i = i+2;
print(sb)