number_to_check = int(input("Введите число, которое нужно проверить на четность или нечетность: "))

if number_to_check % 2 == 0:
    print(f"{number_to_check} - это четное число")
else:
    print(f"{number_to_check} - это нечетное число")