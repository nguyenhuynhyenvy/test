
diem=float(input('Nhập điểm:'))
hanhkiem=str(input('Nhập hạnh kiểm:'))

if hanhkiem in ['tốt','tot','tốt','tot','tốt','tot']:
    hanhkiem = '1'
elif hanhkiem in ['khá','kha','khá','khá']:
    hanhkiem = '2'
elif hanhkiem in ['yếu','yeu','yếu']:
    hanhkiem = '3'
else:
    hanhkiem = '4'

if diem>=8:
    if hanhkiem == "1":
        print('Giỏi')
    if hanhkiem == '2':
        print('khá')
    else:
        print('Trung bình')
elif diem >= 6.5:
    if hanhkiem in ['1', '2']:
        print('Khá')
    else:
        print('Trung bình')
elif diem >=5:
    if hanhkiem!='3':
        print('Trung bình')
    else:
        print('Yếu')
else:
    print('Kém')