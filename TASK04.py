# По заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

X=int(input('Ввведите номер четверти (1, 2, 3, 4):'))

if X==1:
    print('x>0 and y>0')
elif X==2:
    print('x>0 and y<0')
elif X==3:
    print('x<0 and y<0')
elif X==4:
    print('x<0 and y>0')
else:
    print('Вы не правильно ввели четверть')