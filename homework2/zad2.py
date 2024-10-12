squares = []
a = input("Введите первое число: ").replace(',','.')
b = input("Введите второе число: ").replace(',','.')
if a.isalpha()==True or b.isalpha()==True:
    print('ошибка!')
elif a.isnumeric()==True and a.isnumeric()==True:
    a = int(a); b = int(b)
    a +=1
    for i in range(a, b):
        squares.append(i**2)
print(f"Список квадратов целых чисел между {a-1} и {b}: {squares}")