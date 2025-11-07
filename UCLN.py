a=int(input('Nhập số a: '))
b=int(input('Nhập số b: '))
n=1
if a>b:
    c=b
else:
    c=a
for i in range(2,c):
    if b%i==0 and a%i==0:
        n=i
print('ước chung lớn nhất',n)


