# friends = {"Rolf","Bob","Anne"}
# friends.add("Jen")
# print(friends) # Kết quả là {"Bob","Jen","Anne","Rolf"}

a = {1,2,3,4,5,6,7,8,9,10}
b = {5,6,7,8,9,10,11,12,13}

if a & b != set():
    print("Nhung sinh vien dang ki hoc ca 2 ban: ",a & b)
else:
    print("Khong co sinh vien nao dang ki hoc 2 ban")

print("Danh sach sinh vien dang ki: ",a | b)
print("Nhung sinh vien dang ki ban 1 nhung khong dang ki ban 2: ",a - b)