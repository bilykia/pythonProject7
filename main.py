ticket=int(input("Количество билетов:"))
print(ticket)
i = 1
sum_tickets = 0
while i <= ticket:
    age=(int(input(f"Введите возраст посетителя {i}:")))
    print(age)
    if age < 18:
        print ("Билет бесплатный")
        price = 0
    if 25 >= age >= 18:
        print ("Стоимость билета 990 руб.")
        price = 990
    if age >25:
        print("Полная стоимость билета 1390 руб")
        price = 1390
    i += 1
    sum_tickets += price
if ticket > 3:
    print("Сумма с учетом скидки 10%", sum_tickets*0.9)
else:
    print(sum_tickets)
