def uoc_chung(a,b):
    ds=[]
    for i in range (1,min(a,b)):
        if a%i==0 and b%i==0:
            ds.append(i)
    return ds

a=int(input('nhập số:'))
b=int(input('nhập số:'))
print('kết quả',uoc_chung(a,b))
