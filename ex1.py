age = int(input("please enter your age: "))
price = 0

if age >= 40:
    price = 25

elif age >= 30:
    price = 20

elif age >= 20:
    price = 15

elif age >= 10:
    price = 10

else:
    price = 5

print(f"The ticket price is ${price}.")
