#1.Strings
string = " Ankit Singh"
print(len(string))
print(string.upper())
print(string.lower())
print(string.strip())
print(string.capitalize())
print(string.split(" "))
print(string.replace("Ankit", "Atul"))
print(string.find("Ankit"))
print(string.isdigit())
print(string.partition("Singh"))
print(string.istitle())
print(string.casefold())
print(string.center(5))
print(string.zfill(2))

print("-----------------------------------------")
#2. list
list1 = [1, 2, 3, 5, 10, 7, 6]
list1.append(4)
print(list1)
list1.remove(2) # pop the element
print(list1)
list1.sort()
print(list1)
list1.copy()
print(list1)
x= list1.index(3)
print(x)
list1.pop(3) # pop on the index
print(list1)

print("-----------------------------")
decimal = 255

binary = bin(decimal)
octal = oct(decimal)
hexadecimal = hex(decimal)

print(binary)

print('A series of characters designated as one object known as a string' [::-1][4::3])
print("------------")
print('Welcome to Python traing program'[3:10][:: -1] )

# ----------------------------------------------------------

phrase = "was it a car or a cat i saw"
k= phrase[4:23].upper()
print(phrase[0:3].upper(),k[::-1],phrase[24:28].upper())

#-----------------------------------------------------------

X = 2
Z_count = X
O_count = 2 * X

word = "Z" * Z_count + "O" * O_count

print(word)

#-----------------------------------------------------------
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

matrix3 = [[] for _ in range(len(matrix1))]

# Addition
for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        matrix3[i].append(matrix1[i][j] + matrix2[i][j])

for row in matrix3:
    print(row)

# Multiplication
matrix3 = [[] for _ in range(len(matrix1))]  # Reset matrix3

for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        matrix3[i].append(matrix1[i][j] * matrix2[i][j])

for row in matrix3:
    print(row)

# Subtraction
matrix3 = [[] for _ in range(len(matrix1))]  # Reset matrix3

for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        matrix3[i].append(matrix1[i][j] - matrix2[i][j])

for row in matrix3:
    print(row)

