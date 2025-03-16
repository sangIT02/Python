import math

a = float(input("Nhap he so a: "))
b = float(input("Nhap he so b: "))
c = float(input("Nhap he so c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phuong trinh co vo so nghiem")
        else:
            print("Phuong trinh vo nghiem")
    else:
        print("Phuong trinh co nghiem x = ", -c/b)
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("phuong trinh vo nghiem")
    elif delta == 0:
        print("phuong trinh co nghiem kep: x1 = x2 = ", -b/(2*a))
    else:
        x1 = (-b - math.sqrt(delta))/(2*a)
        x2 = (-b + math.sqrt(delta))/(2*a)
        print("Phuong trinh co 2 nghiem phan biet:\n"
              f"x1 = {x1}\n"
              f"x2 = {x2}")
