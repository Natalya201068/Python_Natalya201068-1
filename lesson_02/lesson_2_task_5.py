def month_to_season(month_num):
    if month_num == 1 or month_num == 2 or month_num == 12:
        print("Зима")
    elif month_num == 3 or month_num == 4 or month_num == 5:
        print("Весна")
    elif month_num == 6 or month_num == 7 or month_num == 8:
        print("Лето")
    elif month_num == 9 or month_num == 10 or month_num == 11:
        print("Осень")
    else:
        print("Неверный номер")


month_num = int(input("Введите номер месяца: "))
month_to_season(month_num)

