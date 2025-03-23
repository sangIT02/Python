import math


def checkSNT(n):
    if n < 2 or n > 10000000:
        return False
    else:
        for i in range(2, int(math.sqrt(n))):
            if n % i == 0:
                return False
    return True

def checkDoiXung(n):
    n = str(n)
    if len(n) < 2:
        return False
    l, r = 0, len(n)-1
    while l <= r:
        if n[l] == n[r]:
            l += 1
            r -= 1
        else:
            return False
    return True

while True:
    e = int(input("Nhap so nguyen E khong qua 8 chu so: "))
    s = int(input("Nhap so nguyen S: "))
    if e <= 10000000 and s < e:
        break
    print("so nguyen E co khong qua 8 chu so va so nguyen S < E, moi nhap lai!")

tong = 0
for i in range(s, e):
    if checkSNT(i) and checkDoiXung(i):
        print(i)
        tong += i
print("Tong = ",tong)