#Write a Python program to convert temperatures to and from Celsius,Fahrenheit

print("TEMPERATURE CONVERTER.")
print("FAHRENHEIT IN TO CELSIUS.")

Fahrenheit = int(input("Enter a temperature in Fahrenheit: "))

formula = (Fahrenheit - 32) * 5.0/9.0

print("Temperature:", Fahrenheit, "Fahrenheit = ", formula, " Celsius")