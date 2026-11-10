count = 0
total = 0

while True:
    value = input()

    if value == "stop":
        break

    price = int(value)
    count += 1
    total += price

if count == 0:
    print("Нет покупок")
else:
    average = total / count

    print(f"Покупок: {count}")
    print(f"Общая стоимость: {total} руб")
    print(f"Средняя стоимость: {average:.2f} руб")