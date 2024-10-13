a = float(input("Введите первое число: "))#.replace(',','.')
b = float(input("Введите второе число: "))#.replace(',','.')
#if a.isalpha()==True or b.isalpha()==True:
#    print('ошибка!')
#else:
c = int(a) + (1 if a > int(a) else 0)
d = int(b) + (1 if b > int(b) else 0)
squares = []
for i in range(c,d):
    squares.append(i**2)
print(f"Список квадратов целых чисел между {float(a)} и {float(b)}: {squares}")