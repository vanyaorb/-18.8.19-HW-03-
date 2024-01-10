tickets = int(input("Введите количество билетов: "))

if tickets < 0:
    print("Количество билетов НЕ должно быть отрицательным.")
    exit()

total_cost = 0

for i in range(tickets):
    age = int(input("Введите возраст посетителя: "))

    if age < 0:
        print("Возраст НЕ должен быть отрицательным.")
        exit()

    if age < 18:
        ticket_cost = 0
    elif 18 <= age < 25:
        ticket_cost = 990
    else:
        ticket_cost = 1390

    total_cost += ticket_cost

# Подсчет скидки, если количество билетов больше 3
if tickets > 3:
    discount = 0.1 * total_cost
    total_cost -= discount

print(f"Общая стоимость билетов: {total_cost} руб.")