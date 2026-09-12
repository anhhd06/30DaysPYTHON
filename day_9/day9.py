age = input('nhap tuoi cua toi: ')
if int(age) >= 18 :
    print('Ban da du tuoi lai xe.')
else :
    print('Ban chua du tuoi lai xe.')


your_age = input('Nhap tuoi cua ban: ')
if age > your_age :
    print('Toi lon hon ban {} tuoi.'.format(int(age) - int(your_age)))
elif age < your_age :
    print('Ban lon hon toi {} tuoi.'.format(int(age) - int(your_age)))
else :
    print('toi va ban bang tuoi nhau.')
