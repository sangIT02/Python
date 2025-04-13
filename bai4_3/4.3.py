a = {
    1:1,
    2: 1.5,
    3: 2.0,
    4: 2.5,
    5: 3.0,
    6: 3.5,
    7: 4.0,
    8: 0.5,
    9: 2.2,
}
tong = 0
for i in a:
    if a[i] >= 2.5 and a[i] <= 3.5:
        tong += 1
print("Tong so sinh vien co diem [2.5 , 3.5] la: ",tong)

a[10] = 1.1
print(a)

for i in a.copy():
    if a[i] < 2.0:
        a.pop(i)
print(a)