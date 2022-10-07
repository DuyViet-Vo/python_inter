def UCLN(a,b):
    while(a!=b):
        if a>b:
            a= a-b
        else:
            b=b-a
    
    return a

def BCNN(a,b):
    return (a*b)/UCLN(a,b)


a= int(input('nhap a: '))
b= int(input('nhap b: '))
print('Ước chung lon nhat: ',UCLN(a,b))
print('Bội chung nhỏ nhất: ',BCNN(a,b))
    