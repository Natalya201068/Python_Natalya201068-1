def is_year_leap(year: int) -> bool:
    return True if year % 4 == 0 else False

y = int(input("Введите год: "))
result = is_year_leap(y)
print(f"год {y} : {result}")
