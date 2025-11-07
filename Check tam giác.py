#check tam giác
a=int(input('Nhập số đo cạnh a:'))
b=int(input('Nhập số đo cạnh b:'))
c=int(input('Nhập số đo cạnh c:'))
if a+b>c or a+c>b or b+c>a:
    print('tam giác thường')
    if a==b or a==c or b==c:
        print('tam giác cân')
    if a==b==c:
        print('tam giác đều')
if a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
    print('tam giác vuông')
    if a==b or a==c or b==c:
        print('tam giác vuông cân')
else:
    print('không phải tam giác')