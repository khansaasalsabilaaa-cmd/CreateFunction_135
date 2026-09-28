def convert_temperature(value, unit):
    if unit == 'C':
        return = (value * 9/5) + 32
    elif unit == 'F':
        return = (value - 32) * 5/9
    else:
        return "Unit tidak valid"

# Input
temperature = float(input("Masukkan suhu: "))
unit = input("Masukkan unit (C/F): ").upper()

result = convert_temperature(temperature, unit)

if unit == 'C':
    print("Suhu dalam Fahrenheit:", result)
elif unit == 'F':
    print("Suhu dalam Celsius:", result)
else:
    print(result)