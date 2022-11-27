def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    return False


m = int(input('nhập số hàng: '))
n = int(input('nhập số cột" '))
vt = []
martin = [[int(input()) for _ in range(n)] for _ in range(m)]
for i in range(0, m):
    for j in range(0, n):
        if is_prime(martin[i][j]):
            vt.append('['+str(i)+','+str(j)+']')
print(martin)
print('vi tri: ', ','.join(vt))
