# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
#
# print(thistuple)


a = ("0","1", "2", "3", "4", "5", "6", "7", "8", "9")
a = tuple(int(i) for i in a)
tong = 0
for i in a:
    tong += i
print("Trung binh cong: ", tong/len(a))