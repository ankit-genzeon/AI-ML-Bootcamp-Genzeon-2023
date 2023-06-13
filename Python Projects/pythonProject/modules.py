#modules
import math as m
print(m.pi)
print(m.e)
print(m.sqrt(567))
print(m.factorial(67))
print(m.sin(30))
print(m.degrees(34))

#sys
import sys
print(sys.path)

#os
import os
os.mkdir("hello")
os.rmdir("hello")

#stats
import statistics as st
print(st.mean([23,432,56,21]))
print(st.mode([1,2,3,4,5,6,78,2]))
print(st.median([2,456,7,92,25,7]))

#random
import random as r
print(r.randrange(1,50))
print(r.random())
print(r.randint(1,100))

gn=r.randint(1,10)
gn2=int(input("guess the numbers"))
if gn2==gn:
    print("party de")
else:
    print("bachgaya")

