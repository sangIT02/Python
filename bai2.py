import math

print("Nhap toa do diem A:")
x1 = float(input("nhap x1: "))
y1 = float(input("nhap y1: "))

print("Nhap toa do diem B:")
x2 = float(input("nhap x2: "))
y2 = float(input("nhap y2: "))

d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
m = math.fabs(x2 - x1) + math.fabs(y2 - y1)
c = 1 - (x1*x2 + y1*y2)/(math.sqrt(x1**2 + y1**2) * math.sqrt(x2**2 + y2**2))

print("Khoang cach Eulidean giua A va B la: ", d)
print("khoang cach Manhattan giua A va B la: ", m)
print("Khoang cach Cosin giua A va b la: ", c)
