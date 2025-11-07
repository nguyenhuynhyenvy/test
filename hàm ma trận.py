m = int(input("Nhập số hàng của A: "))
n = int(input("Nhập số cột của A (số hàng của B): "))
p = int(input("Nhập số cột của B: "))

A = []
print("ma trận A")
for i in range(m):
    row = []
    for j in range(n):
        x = int(input(f'nhập phần tử hàng {i+1}:'))
        row.append(x)
    A.append(row)
print("A=")
for row in A:
    print(row)


B=[]
print("ma trận B")
for j in range(n):
    row = []
    for k in range(p):
        y = int(input(f'nhập phần tử hàng {j+1}:'))
        row.append(y)
    B.append(row)
print("B=")
for row in B:
    print(row)


C = []
for i in range(m):
    row = []
    for j in range(p):
        row.append(0)
    C.append(row)
for i in range(m):
    for j in range(p):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]


print("Ma trận C là:")
for row in C:
    print(row)
