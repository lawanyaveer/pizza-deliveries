#100 days of python bootcamp
#3rd day
#pizza delivery


print("welcome to python pizza deliveries")
size = input("which size pizza do you want? S , M , L")
add_pepperoni = input("do you want pepperoni ? y or n")
extra_cheese = input("do you want extra cheese? y or n")
Bill = 0
if size == "S":
    Bill += 15
elif size == "M":
    Bill += 20
else:
    Bill += 25
if add_pepperoni == "y":
    if size == "S":
        Bill += 2
    else:
        Bill += 3
if extra_cheese =="y":
    Bill += 1
print(f"your final bill is ${Bill}")
