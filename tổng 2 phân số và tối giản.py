a=int(input('nhập tử số 1: '))
b=int(input('nhập mẫu số 1: '))
c=int(input('nhập tử số 2: '))
d=int(input('nhập mẫu số 2: '))
tu=a*d+b*c
mau=b*d
tu1=tu
mau1=mau
if tu1>mau1:
    c=mau1
else:
    c=tu1
for i in range(1,c+1):
    if tu1%i==0 and mau1%i==0:
        n=i
tumoi=tu1//n
maumoi=mau1//n
print('phân số là',tumoi,'/',maumoi)



