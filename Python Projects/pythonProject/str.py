import sys

print("Hello World")
a= 'hello'
print (a)

#strings are array
b = "my name is ankit"
print(b[3]) # will print "n"

#loop through string
for x in "Ankit" :
    print(x, end="")
   # sys.stdout.write(x) #to print in one line

# length of string
print(len("Ankit"))

#multiple line sprint
s= '''my name is anthony gonzalves
main duniya mein akela hu
dil bhi hai khaali 
ghar bhi hai khaali'''
print(s)

#not in
genzeon = "sudhanshu is in office"
if"ankit" not in genzeon :
    print("siva angry")

#remove white spaces
txt = "  hi my name   "
print(txt.strip())

#see some slicing
slice = " Ankit Singh"
print(slice[1:2]) # 2nd point is n-1
print(slice[1:5:3])