#tính thuế thu nhập cá nhân
a=float(input('Thu nhập tính thuế trong tháng (triệu đồng): '))
if a<=5:
    b=a*0.05
    print('Tiền thuế khi đó là', b, 'triệu đồng')
elif a<=10:
    b=a*0.1
    print('Tiền thuế khi đó là', b, 'triệu đồng')
elif a<=18:
    b=a*0.15
    print('Tiền thuế khi đó là', b, 'triệu đồng')
elif a<=32:
    b=a*0.2
    print('Tiền thuế khi đó là', b, 'triệu đồng')
elif a<=52:
    b=a*0.25
    print('Tiền thuế khi đó là', b, 'triệu đồng')
elif a<=80:
    b=a*0.3
    print('Tiền thuế khi đó là', b, 'triệu đồng')
else:
    b=a*0.35
    print('Tiền thuế khi đó là', b, 'triệu đồng')