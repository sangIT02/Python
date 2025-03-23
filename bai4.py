import math

print("Nhap tao do diem A:")
x1 = float(input("nhap x1: "))
y1 = float(input("nhap y1: "))

print("Nhap tao do diem B:")
x2 = float(input("nhap x2: "))
y2 = float(input("nhap y2: "))

print("Nhap tao do diem B:")
x3 = float(input("nhap x3: "))
y3 = float(input("nhap y3: "))

dA = math.sqrt(x1**2 + y1**2)
dB = math.sqrt(x2**2 + y2**2)
dC = math.sqrt(x3**2 + y3**2)


if dB < dA and dC < dA:
    print("Diem xa tam O nhat la A: ",dA)
    if dB > dC:
        print("Diem gan tam O nhat C: ",dC)
    else:
        print("Diem gan tam O nhat B: ",dB)
elif dC > dB and dC > dA:
    print("Diem xa tam O nhat la C: ", dC)
    if dB > dA:
        print("Diem gan tam O nhat A: ", dA)
    else:
        print("Diem gan tam O nhat B: ", dB)
else:
    print("Diem xa tam O nhat la B: ", dB)
    if dC > dA:
        print("Diem gan tam O nhat A: ", dA)
    else:
        print("Diem gan tam O nhat C: ", dC)

ab = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
ac = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
cb = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
p = (ab + ac + cb)/2
s = math.sqrt(p*(p - ab)*(p - ac)*(p -cb))
print("Dien tich tam giac ABC la: ",s)