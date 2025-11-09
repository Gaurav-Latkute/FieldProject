#  Que5. Write a program to input temperature in Celsius and convert it into Fahrenheit.

# Take Input from user
celsius = float(input("Enter Temperature in Celsius: "))

# Convert Celcius to Fahrenheit
far = (celsius * 9/5) + 32

# Display Result
print(f"{celsius}°C is equal to {far}°F")