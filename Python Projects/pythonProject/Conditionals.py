#decision making
#if Statement
# var = 10
# if var>0:
#     print("true")
#     print(var)
#
# #ifelse
# var1=-1
# if var1>0:
#     print("true")
# else:
#     print("false")

#ticket booking with if else
# age = int(input("Enter your age: "))
# if age < 0:
#     print("Invalid age")
# elif age <= 3:
#     print("Ticket is free")
# elif age <= 12:
#     print("Ticket price: $10")
# elif age <= 18 and age <=60:
#     print("Ticket price: $15")
# else:
#     print("Ticket price: $20/2")

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
else:
    if age <= 3:
        print("Ticket is free")
    else:
        if age <= 12:
            print("Ticket price: 10")
        else:
            if age <= 18:
                print("Ticket price: 15")
            else:
                print("Ticket price: 20")

