train_data = input()
parts = train_data.split(";")

train_number = parts[0]
departure_city = parts[1]
arrival_city = parts[2]
departure_time = parts[3]
price = float(parts[4])
print(f"Поезд: {train_number}")
print(f"Маршрут: {departure_city} - {arrival_city}")
print(f"Цена: {price:.2f} руб")
