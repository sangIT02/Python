TAP = "-av-bvc,-bv-cvd,a,b,-e"
TAP = "-av-bvc,-gvd,-cvd,a,b,-d"

def phu(x):
    if x[0] == '-':
        return x[1:]
    else:
        return '-' + x


def res(a, b):
    check = False
    ans = list(set(a+b))
    for i in ans[:]:
        if phu(i) in ans:
            ans.remove(i)
            ans.remove(phu(i))
            check = True
    return sorted(ans), check

def robinson(TAP):
    TAP = TAP.split(",")
    so = 1
    my_dict = {}
    for menh_de in TAP:
        my_dict[so] = sorted(menh_de.split("v"))
        so += 1
    for key, val in my_dict.items():
        print("{:>3}.   {}".format(key,val))

    da_duyet = set()
    for i in list(my_dict.keys()):
        for j in list(my_dict.keys())[i:]:
            if (i, j) not in da_duyet:
                tam, check = res(my_dict[i],my_dict[j])
                da_duyet.update({(i, j), (i, so), (j, so)})
                if not check:
                    continue
                if not tam:
                    print("{:>3}. Res({:>2}, {:>3}) = {}".format(so,i,j,tam))
                    print("=> vậy bài toán được chứng minh.")
                if tam not in my_dict.values():
                    print("{:>3}. Res({:>2}, {:>3}) = {}".format(so,i,j,tam))
                    my_dict[so] = tam
                    so += 1
    return  False

print(robinson(TAP))