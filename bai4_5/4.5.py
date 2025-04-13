dic = {
    "n": "1500",
    "CLUSTERS": "3",
    "ITER": "1000",
    "METHOD": "DCA CLUSTERING",
    "MEASURE": "EUCLIDEAN",
    "YEARS": "9",
    "MAX": "200"
}
print(dic)
dic["MEASURE"] = "MANHATAN"
print(dic)
print("Thong so METHOD: ", dic["METHOD"])

dic["LOSS FUNCTION"] = "SOFT MAX"
print(dic)

dic.pop("YEARS")
print(dic)

s = str(input("Nhap sau S: "))

for i in dic:
    w = str(dic[i])
    if w.find(s) != -1:
        print("S trung voi thong so: ",i)

set1 = {dic[i] for i in dic}
print(set1)
l = [dic[i] for i in dic]
print(l)