arr=[]
for i in range(10,200):
    if(i%7==0 and i%5!=0):
        arr.append(str(i))
print(",".join(arr))