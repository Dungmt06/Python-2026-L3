celsius = float(input("Enter the temperature in Celsius? "))
fahrenheit = (celsius * 9/5) + 32
c_display = int(celsius) if celsius.is_integer() else celsius
print(f"{c_display} (C) = {fahrenheit:.1f} (F)")