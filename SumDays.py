sumall = 0
def digit_sum(n):
    return sum(int(d) for d in str(n))
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def month_digit_sums(year):
    if year % 4 == 0:
        days_in_month[1] = 29
    else:
        days_in_month[1] = 28
    month_sums = [0] * 12
    for month, days in enumerate(days_in_month):
        for day in range(1, days + 1):
            month_sums[month] += digit_sum(day)
    return month_sums

year = int(input("Введите год: "))
digit_sums = month_digit_sums(year)
month_names = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
               'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
for i, sum in enumerate(digit_sums):
    print(f"{month_names[i]}: {sum}")
    sumall+=sum
print("Сумма всех месяцев -",sumall)