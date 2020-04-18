name = input("enter first name..")
name_2 = input("enter second name")

print(name)
age = input("enter his/her age...")
print(name_2)
age_2 = input("enter his/her age...")

if age < age_2:
    print(name, "is younger than", name_2)

elif age == age_2:
    print(name, "and", name_2, "are of same age")

else:
    print(name, "is elder than", name_2)