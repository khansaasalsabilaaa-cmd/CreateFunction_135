def convert_temperature(value, unit):
    if unit == 'C':
        fahrenheit = (value * 9/5) + 32
        return fahrenheit
    elif unit == 'F':
        celsius = (value - 32) * 5/9
        return celsius
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