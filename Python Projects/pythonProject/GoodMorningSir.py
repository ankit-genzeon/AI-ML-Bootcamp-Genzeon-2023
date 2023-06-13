import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime('%H'))
print(hour)
if  4<= hour <=12 :
    print("Good Morning Sir")
elif 12< hour < 16:
    print("Good Afternoon Sir")
elif 16<= hour < 22:
    print("Good Evening Sir")
else:
    print("Goodnight")