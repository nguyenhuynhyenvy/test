#Tổng các số cữ số cần tính
n=int(input('Nhập các chữ số cần tính tổng: '))
k=[]
i=0
while i<n:
    a=int(input('Nhập số: '))
    k.append(a)
    i=i+1
S=0
while i<n:
    S=S+k[i]
    i=i+1
print('Tổng:',S)