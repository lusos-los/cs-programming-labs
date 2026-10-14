full_name = input()
parts = full_name.split()

surname = parts[0].capitalize()
first_initial = parts[1][0].upper()
middle_initial = parts[2][0].upper()

print(f"{surname} {first_initial}. {middle_initial}.")