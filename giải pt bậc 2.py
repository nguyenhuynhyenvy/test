#input
import math
a=float(input('Nhập hệ số a:'))
b=float(input('Nhập hệ số b:'))
c=float(input('Nhập hệ số c:'))
songhiem=00000



#process
if a==0:
    if b==0:
        if c==0:
            songhiem=888
        else:
            songhiem=0
    else:
        xx=-c/b
        print('xx=',xx)
if a!=0:
    d=b*b-4*a*c
    if d<0:
        songhiem=0
    if d==0:
        x=-b/(2*a)
        songhiem=11
    if d>0:
        x1=(-b+math.sqrt(d))/2*a
        x2=(-b-math.sqrt(d))/2*a
        songhiem=2



#output
if songhiem==888:
    print('pt vô số nghiệm')
if songhiem==0:
    print('pt vô nghiệm')
if songhiem==11:
    print('phương trình có nghiệm kép x=', x)
if songhiem==2:
    print('Phương trình có 2 nghiệm x1=', x1, 'x2=', x2)