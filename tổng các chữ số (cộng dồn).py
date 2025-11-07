#Tổng các số cữ số cần tính
n=int(input('Nhập số các chữ số cần tính tổng'))
S=0
i=1
while i<n:
    a=int(input('Nhập số cần tính:'))
    S=S+a
    i=i+1
print('tổng:',S)