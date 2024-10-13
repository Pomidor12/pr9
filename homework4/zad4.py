#Пользователь вводит числа до тех пор, пока не введет слово ‘end’. 
#Поместите введенные числа в список. Подсчитайте количество 
#четных и нечетных элементов в списке.
numbers = []
g = 0
f = 0
while True:
    user_input = input("Введите число (или 'end' для завершения): ")
    if user_input == "end":
        break
    elif user_input.isalpha() == True or user_input.find(',')>0 or user_input.find('.')>0:
        print("Некорректный ввод")
    else:
        numbers.append(int(user_input))
for number in numbers:
    if number % 2 != 0:
        g += 1
    else:
        f += 1
print(f'Количество четных чисел: {g}\nКоличество четных чисел: {f}')    