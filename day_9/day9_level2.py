'''
90-100, A
80-89, B
70-79, C
60-69, D
0-59, F
'''


Diem = input('Nhap diem cua ban: ')
Diem = int(Diem)
if Diem>=90:
    print('A')
elif Diem>=80:
    print('B')
elif Diem>=70:
    print('C')
elif Diem >=60:
    print('D')
else:
    print('F')
