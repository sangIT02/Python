import math

x = float(input("Nhap so thuc x: "))
n = int(input("Nhap so nguyen n: "))


if n % 2 == 1:
    print("S = 0")
else:
    s = 2016*x
    for i in range(2, n+1):
        s += x**i/3**(i - 1)
    print("S = ", s)