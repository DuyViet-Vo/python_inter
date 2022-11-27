lst = list(map(str,input().split()))
lst.sort()
lst.reverse()
for i in lst : 
    print(i,end='')