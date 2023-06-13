import phonenumbers
from phonenumbers import timezone, geocoder, carrier
#taking input from user
number=input("Enter your number with +: ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone,"en")
reg = geocoder.description_for_number(phone,"en")
print(phone)
print(time)
print(reg)
print(car)
