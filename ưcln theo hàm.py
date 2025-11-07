def ucln(a,b):
    for i in range(min(a,b),0,-1):
        if b%i==0 and a%i==0:
            return i

a=int(input('Nhập số cần tính:'))
b=int(input('Nhập số cần tính:'))
print('Kết quả:',ucln(a,b))

'''def ucln(a,b):
    i=1
    if a>b:
        c=b
    else:
        c=a
    while i<=c:
        if b%i==0 and a%i==0:
            n=i
        i+=1
    return n
a=int(input('Nhập số cần tính:'))
b=int(input('Nhập số cần tính:'))
print('Kết quả:',ucln(a,b))'''
