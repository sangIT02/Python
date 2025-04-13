s = str(input("Nhap chuoi: "))
q = " nguyen van sang"

if q.find(s) == -1:
    print(f"s khong phai sau con cua q: S = {s}, Q = {q}")
else:
    print(f"s la sau con cua q: S = {s}, Q = {q}")
print(s)

p = s + q
print(p)
if p.find("Ha") != -1:
    p = p.replace("Ha","Ba")
print(p)

w = p.split(" ")
keys = [i for i in range(0, len(w))]
dic = dict(zip(keys, w))
print(dic)