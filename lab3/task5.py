identifier = input()

print(f"Длина: {len(identifier)}")
print(f"Только буквы: {identifier.isalpha()}")
print(f"Только цифры: {identifier.isdigit()}")
print(f"Буквенно-цифровая: {identifier.isalnum()}")
print(f"Содержит дефис: {'-' in identifier}")