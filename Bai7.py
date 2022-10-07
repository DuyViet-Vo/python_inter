import math
def isNguyenTo(n):
    if(n<2):
        return False;
    v = int(math.sqrt(n));
    for i in range(2,v+1):
        if(n%i==0):
            return False;
        return True;
n= int(input('nhập giá trị n='))
print(n, 'số nguyên tố đầu tiên là: ')
dem = 0
i =2 
sb= ""
while(dem<n):
    if(isNguyenTo(i)):
        sb = sb + str(i)+" "
        dem +=1
    i+=1
print(sb)