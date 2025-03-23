import module1 as md1

def ConvertForeignCurrency(a, b):
    tongvnd = a*b
    totalusd = tongvnd/md1.usd
    totalyen = tongvnd/md1.yen
    totalcny = tongvnd/md1.cny
    return f"usd: {round(totalusd,2)}, yen: {round(totalyen,2)}, cny: {round(totalcny)}"

a = float(input("Nhap so dam bay: "))
b = float(input("Nhap so tien VND/ 1 dam bay: "))
print(ConvertForeignCurrency(a,b))