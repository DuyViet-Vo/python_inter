def tongCacChuSo(n):
    total = 0;
    while(n>0):
        total = total + n%10;
        n = int(n/10);
    return total;

n = int(input('nhập số n: '))
print('tổng các chữ số ',n,'là : ',tongCacChuSo(n))