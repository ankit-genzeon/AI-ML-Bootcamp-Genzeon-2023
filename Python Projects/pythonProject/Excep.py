try:
    print(x)
except:
    print("aagya")
else:
    print("blah")
finally:
    print("finally")

#raise an exception
def vote_eli(age):
    if age < 18:
        raise Exception("vote ille")
    else:
        print("vote krle")

try:
    age = int(input("Enter your age: "))
    vote_eli(age)
except ValueError:
    print("Sahi Daal")
except Exception as e:
    print(e)
