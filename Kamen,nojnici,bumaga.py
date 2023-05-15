a = input()
b = input()
if a == b:
    print('ничья')
elif a == 'камень' and (b == 'ножницы' or b == 'ящерица'):
    print('игрок a')
elif a == 'ножницы' and (b == 'бумага' or b == 'ящерица'):
    print('игрок a')
elif a == 'бумага' and (b == 'камень' or b == 'Спок'):
    print('игрок a')
elif a == 'ящерица' and (b == 'Спок' or b == 'бумага'):
    print('игрок a')
elif a == 'Спок' and (b == 'камень' or b == 'ножницы'):
    print('игрок a')
else:
    print('игрок b')