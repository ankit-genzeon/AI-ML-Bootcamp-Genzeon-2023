#set
s1={1,3}
s2={1,2,3,"hi", (1,2,3,4,)}
l=[1,4,6,7]
s3= set(l)
print(s3)

s1.add(2)
print(s1)

s1.update([2,3,4])
print(s1)

s1.discard(4) #discard removes the specified items from the set
print(s1)

# s1.remove(4) #remove will raise an error if item is not present
# print(s1)

#set operations
a={1,2,3,4}
b={4,5,6,7}

a.update([10,11,34])
#difference
c= a.difference(b)#only exist in a not in b
print(c)
e= b.difference(a) #only exist in b not in a
print(e)
g=a.difference_update(b)
print(g)
#intersection
f= a.intersection(b) # returns that exist in both the set
print(f)
#union
d=a.union(b)
print(d)

z=a.issubset(b)
print(z)

#Dictionary
car =  {"brand":"ford",
        "model":"mustang",
        "year": 2005}
x= car.get("model")
print(x)
y=car.items()
print(y)
z=car.keys()
print(z)
m = car.setdefault("model", "truck")
print(m)
n= car.values()
print(n)


