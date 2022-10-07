import math
def isNguyenTo(n):
    if(n<2):
        return False;
    v = int(math.sqrt(n));
    for i in range(2,v+1):
        if(n%i==0):
            return False;
        return True;
for i in range(10000,99999):
        if(isNguyenTo(i)):
            print(i)
            