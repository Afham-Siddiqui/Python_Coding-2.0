"""Write a Python program to calculate body mass index."""

print("BMI CALCULATOR.")

wgt_unit = input("YOU HAVE TO ENTER YOUR WEIGHT IN 'kg' OR 'lbs..? ")
wgt_unit = wgt_unit.lower()
weight = float(input("ENTER YOUR WEIGHT: "))

hgt_unit = input("YOU HAVE TO ENTER YOUR HEIGHT IN 'm' OR 'in..? ")
hgt_unit = hgt_unit.lower()
height = float(input("ENTER YOUR HEIGHT: "))

if wgt_unit == "kg" and hgt_unit == "metres":
    BMI = weight/(height**2)
    print("YOUR BMI IS", weight)

elif wgt_unit == "lbs" and hgt_unit == "in":
    BMI = (703 * weight) / (height**2)
    print("YOUR BMI IS", weight)

if weight < 18.5:
    print("YOU ARE UNDERWEIGHT")

elif weight >= 18.5 and weight <= 24.9:
    print("YOU ARE NORMAL")

elif weight > 25 and weight < 29.9:
    print("YOU ARE OVERWEIGHT")

else:
    print("YOU ARE OBESE")