import pandas as pd
import numpy as np

# Đọc file CSV chứa dữ liệu training
dt = pd.read_csv("knn2.csv")

# Chứa thông tin các phần tử mẫu
p = np.array([dt['chay'], dt['sut']])

# Chứa loại của các phần tử mẫu
t = np.array([dt['loai']])

# Chứa thông tin phần tử training
p = p.T

# Chứa lớp của các phần tử training
t = t.T

# Phần tử test
test = np.array([[7, 7]])

# Bộ trọng số khởi tạo
w = np.array([[-1, 0]])

# Bias khởi tạo
b = -4 

# Các biến khởi tạo
a = 0
k = 0
m = len(p)  # Số phần tử training

while True:
    d = True
    k += 1
    print("Lần lặp thứ", k)
    for i in range(m):
        x = np.array([p[i]])
        n = w.dot(x.T) + b
        if n < 0:
            a = 0
        else:
            a = 1
        if a != t[i]:
            e = t[i] - a
            w=w+np.dot(e,x)
            b=b+e
            d=False
    print("w=",w)
    print("b=",b)
    if(d==True):
        break
n = w.dot(test.T)+b
if n < 0:
    wr="san pham dat yeu cau"
else:
    wr= "san pham khong dat yeu cau"
print("san pham test: "+"\""+wr+"\"")