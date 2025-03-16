import math


def SoNguyenTo(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
    return True

def SoDoiXung(n):
    a = []
    while n != 0:
        a.append(n%10)
        n = int(n/10)
    l,r = 0,len(a)-1
    while l <= r:
        if a[l] == a[r]:
            l += 1
            r -= 1
        else:
            return False
    return True
n = int(input("Nhap so nguyen n it hon 7 chu so: "))
if (SoNguyenTo(n) == True) and (SoDoiXung(n) == True):
    print("hop le")
else:
    print("Khong hop le")