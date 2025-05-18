class Person:
    def __init__(self, ho_ten, ngay_sinh, que_quan):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.que_quan = que_quan

class KYSU(Person):
    def __init__(self, ho_ten, ngay_sinh, que_quan, nganh_hoc, nam_tot_nghiep:int):
        super().__init__(ho_ten,ngay_sinh,que_quan)
        self.nganh_hoc = nganh_hoc
        self.nam_tot_nghiep = nam_tot_nghiep

    # def khoi_tao_thong_tin(self):
    #     self.ho_ten = "Nguyen Van Sang"
    #     self.ngay_sinh = 11
    #     self.que_quan = "Hoa binh"
    #     self.nganh_hoc = "Ki thuat phan mem"
    #     self.nam_tot_nghiep = 2026

    def in_thong_tin(self):
        print(f"Ho ten: {self.ho_ten}")
        print(f"Ngay sinh: {self.ngay_sinh}")
        print(f"Que quan: {self.que_quan}")
        print((f"Nganh hoc: {self.nganh_hoc}"))
        print(f"Nam tot nghiep: {self.nam_tot_nghiep}")

n = int(input("Nhap so ky su: "))
arr = []
for i in range(n):
    print(f"==> Nhap ky su thu: {i+1}")
    ho_ten = str(input("Nhap ho ten: "))
    ngay_sinh = str(input("Nhap ngay sinh: "))
    que_quan = str(input("Nhap que quan: "))
    nganh_hoc = str(input("Nhap nganh hoc: "))
    nam_tot_nghiep = int(input("Nhap nam tot nghiep: "))
    ks = KYSU(ho_ten, ngay_sinh, que_quan, nganh_hoc, nam_tot_nghiep)
    arr.append(ks)

for i in range(n):
    arr[i].in_thong_tin()

max = max(arr[i].nam_tot_nghiep for i in range(n))
print("==>Thong tin ky su tot nghiep gan day la:")
for i in range(n):
    if arr[i].nam_tot_nghiep == max:
        arr[i].in_thong_tin()
