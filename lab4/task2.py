
base_price = float(input())
age = int(input())

if base_price <= 0 or age < 0 or age > 120:
    print("Ошибка")
elif age <= 5:
    price = 0
    print(f"Стоимость: {price:.2f} руб")
elif age <= 17:
    price = base_price * 0.5
    print(f"Стоимость: {price:.2f} руб")
elif age <= 59:
    price = base_price
    print(f"Стоимость: {price:.2f} руб")
else:
    price = base_price * 0.7
    print(f"Стоимость: {price:.2f} руб")

