a = input("Введите первое число: ").replace(',','.')
b = input("Введите второе число: ").replace(',','.')
squares = []
for i in range(round(a), b):
    squares.append(i**2)
print(f"Список квадратов целых чисел между {a} и {b}: {squares}")