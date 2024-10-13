numbers = []
while True:
    user_input = input("Введите число (или 'end' для завершения): ")
    if user_input == "end":
        break
    elif user_input.isalpha() == True or user_input.find(',')>0 or user_input.find('.')>0:
        print("Некорректный ввод")
    else:
        numbers.append(int(user_input))
print("Нечетные числа в списке:", end=" ")
for number in numbers:
    if number % 2 != 0:
        print(number, end=" ")