class CO:
    def addn(self,a,b):
        return a+b
    def subn(self,a,b):
        return a-b

obj=CO()
print("addition is", obj.addn(5,5))
print("substraction",obj.subn(5,4))

# inheritence

#single
class Animal:
    def animal_sound(self):
        return "makes sound"
class Cat(Animal):
    def cat_sound(self):
        return self.animal_sound()+"\meow"
    def __str__(self):
        return "CAT"

class Dog(Animal):
    def dog_sound(self):
        return self.animal_sound()+" bhau"
    def __str__(self):
        return "DOG"

catobj= Cat()
print(catobj,catobj.cat_sound())
dogobj= Dog()
print(dogobj,dogobj.dog_sound())
