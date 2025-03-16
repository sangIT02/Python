a = int(input("nhap so nguyen: "))

b = int(a/1000)
c = int((a - b*1000)/100)
d = int((a - b*1000 - c*100)/10)
e = a%(b+c+d)
print(f"{b} ngan, {c} tram, {d} chuc, {e} don vi")
